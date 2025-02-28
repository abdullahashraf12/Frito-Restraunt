from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from product.models import CardOrderItems,CashierTable
from userauths.models import UserToken  # Adjust the import according to your project structure
import json
import asyncio
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class GetCart(AsyncWebsocketConsumer):

    @sync_to_async
    def get_user_by_token(self, token):
        print(token)

        try:
            return UserToken.get_user_by_token(token)
        except ObjectDoesNotExist:
            return None

    @sync_to_async
    def fetch_cart_items(self, user):
        all_in_cards_for_this_user = list(CardOrderItems.objects.filter(user=user).values())
        get_all_from_card = CardOrderItems.objects.filter(user=user)
        total_price = get_all_from_card.aggregate(total_price=Sum('total_price_for_all'))['total_price']
        data = {
                "items": list(get_all_from_card.annotate(
                    image_url=F('uoc_prod__image')
                ).values(
                    'uoc_prod__title', 'image_url', 'user_meal_type', 'quantity',
                    'MealType', 'MealSideDishes', 'MealAdditions', 'total_price_for_all'
                )),
                "total_price": float(total_price)
            }
        for item in all_in_cards_for_this_user:
            card_order_item = CardOrderItems.objects.get(id=item.get("id"))
            item["product_name"] = card_order_item.uoc_prod.title
            try:
                item["default_image"] = card_order_item.uoc_prod.image.url
            except CardOrderItems.DoesNotExist:
                item["default_image"] = None
        return {'success_cart_data': all_in_cards_for_this_user,"success_checkout_data":data}

    async def get_from_db_to_cart(self, token):
        try:
            user = await self.get_user_by_token(token)
            if user:
                cart_data = await self.fetch_cart_items(user)
                return cart_data
        except Exception as e:
            print(e)
            return None

    async def connect(self):
        print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        user_token = self.scope['cookies'].get('user_token')
        self.room_group_name = None

        if user_token:
            user_token_exists = await sync_to_async(UserToken.objects.filter(token=user_token).exists)()
            if user_token_exists:
                self.room_group_name = user_token

                await self.channel_layer.group_add(
                    self.room_group_name,
                    self.channel_name
                )

                await self.accept()
                print(f"User token connected: {user_token}")
                await self.send_cart_data(user_token)  # Start sending cart data

            else:
                print(f"User token not ergistered")

                await self.close()
        else:
            print(f"User has no token")

            await self.close()

    async def disconnect(self, close_code):
        if self.room_group_name:
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        print(f"Received message: {data}")

    async def send_cart_data(self, token):
        while True:
            try:
                cart_data = await self.get_from_db_to_cart(token)
                if cart_data:
                    json_str = json.dumps(cart_data)
                    await self.send(text_data=json_str)
                await asyncio.sleep(1)  # Wait for 2 seconds before sending the next message
            except Exception as e:
                print(f"Error sending message: {e}")
                break  # Exit the loop on error or close flag




class GetCashierItems(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope["user"].is_staff:
            await self.channel_layer.group_add("cashier_items", self.channel_name)
            await self.accept()
            print("Staff user connected")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("cashier_items", self.channel_name)

    async def send_new_record(self, event):
        await self.send(text_data=json.dumps(event["data"]))

@receiver(post_save, sender=CashierTable)
def update_related_order(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()

    if created:
        print("New row has been created")
        print(instance.get_popup_url())
        async_to_sync(channel_layer.group_send)(
            "cashier_items",
            {
                "type": "send_new_record",
                "data": {
                    "id":instance.pk,
                    "order_number": instance.order_number,
                    "order_date": instance.order_date,
                    "client": instance.client.username,
                    "address": instance.address,
                    "client_number": instance.client_number,
                    "total_price": instance.total_price,
                    "status": instance.client_status,
                    "sales_rep": instance.SalesRep.username if instance.SalesRep else None,
                    "popup_url": instance.get_popup_url(),  # Include popup_url here

                },
            },
        )





class my_orders(AsyncWebsocketConsumer):
    
    async def connect(self):
        print("Connection is establishing")
        user_token = self.scope['cookies'].get('user_token')
        self.room_group_name = None

        if user_token:
            user_token_exists = await sync_to_async(UserToken.objects.filter(token=user_token).exists)()
            if user_token_exists:
                self.room_group_name = user_token

                await self.channel_layer.group_add(
                    self.room_group_name,
                    self.channel_name
                )

                await self.accept()
                print(f"User token connected: {user_token}")
                await self.send_cart_data(user_token)  # Start sending cart data

            else:
                await self.close()
        else:
            await self.close()

    async def disconnect(self, close_code):
        if self.room_group_name:
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        print(f"Received message: {data}")

    async def send_cart_data(self, token):
        while True:
            try:
                cart_data = await self.get_from_db_to_cart(token)
                if cart_data:
                    json_str = json.dumps(cart_data)
                    await self.send(text_data=json_str)
                await asyncio.sleep(1)  # Wait for 2 seconds before sending the next message
            except Exception as e:
                print(f"Error sending message: {e}")
                break  # Exit the loop on error or close flag















# from channels.generic.websocket import AsyncWebsocketConsumer
# from asgiref.sync import sync_to_async
# from product.models import CardOrderItems
# from userauths.models import UserToken  # Adjust the import according to your project structure
# import json
# import asyncio
# from django.http import JsonResponse

# class GetCart(AsyncWebsocketConsumer):

#     @sync_to_async
#     def get_user_by_token(self, token):
#         print(token)
#         print(token)
#         print(token)
#         print(token)
#         print(token)
#         print(token)
#         print(token)
#         print(token)
#         print(token)
#         print(token)
#         print(token)
#         print(token)
#         print(token)
#         print(token)
#         print(token)
#         try:
#             return UserToken.get_user_by_token(token)
#         except UserToken.DoesNotExist:
#             return None

#     async def get_from_db_to_cart(self, token):
#         try:
#             user = await self.get_user_by_token(token)
#             if user:
#                 print(user)

#                 # Uncomment and adapt this block if you need to fetch and process cart items
#                 all_in_cards_for_this_user = list(CardOrderItems.objects.filter(user=user).values())

#                 print("++++++++++++++++++++++++++++++")
#                 print(all_in_cards_for_this_user)
#                 print(all_in_cards_for_this_user)
#                 print("++++++++++++++++++++++++++++++")

#                 # data = []
#                 n=0
#                 for item in all_in_cards_for_this_user:
#                     card_order_item = CardOrderItems.objects.get(id=item.get("id"))

#                     item["product_name"] = card_order_item.uoc_prod.title
#                     try:
#                         item["default_image"] = card_order_item.uoc_prod.image.url
#                     except CardOrderItems.DoesNotExist:
#                         # Handle the case where the CardOrderItems object doesn't exist
#                         item["default_image"] = None  # or any default image URL you want to assign
#                 print(all_in_cards_for_this_user)

                
#                 return {'success': all_in_cards_for_this_user}
#         except Exception as e:
#             print(e)

#     async def connect(self):
#         user_token = self.scope['cookies'].get('user_token')

#         self.room_group_name = None

#         if user_token:
#             user_token_exists = await sync_to_async(UserToken.objects.filter(token=user_token).exists)()

#             if user_token_exists:
#                 self.room_group_name = user_token

#                 await self.channel_layer.group_add(
#                     self.room_group_name,
#                     self.channel_name
#                 )

#                 await self.accept()
#                 print(f"User token connected: {user_token}")
#                 # await self.send()
#                 await self.send_cart_data(user_token)  # Start sending cart data

#             else:
#                 await self.close()
#         else:
#             await self.close()

#     async def disconnect(self, close_code):
#         if self.room_group_name:
#             await self.channel_layer.group_discard(
#                 self.room_group_name,
#                 self.channel_name
#             )

#     async def receive(self, text_data=None, bytes_data=None):
#         data = json.loads(text_data)
#         print(f"Received message: {data}")

#     async def send_cart_data(self,token):
#         json_data = {"user_Cart": "data"}
        
#         while True:
#             try:
#                 print(self.get_from_db_to_cart(token))
#                 json_str = json.dumps(self.get_from_db_to_cart(token))
                
#                 # Replace this with your actual sending logic
#                 await self.send(text_data=json_str)
                
#                 await asyncio.sleep(2)  # Wait for 2 seconds before sending the next message
                
#             except Exception as e:
#                 print(f"Error sending message: {e}")
#                 break  # Exit the loop on error or close flag


# # from channels.generic.websocket import WebsocketConsumer
# # from asgiref.sync import async_to_sync
# # from django.http import JsonResponse
# # from product.models import CardOrderItems
# # from userauths.models import UserToken  # Assuming UserToken model is defined in your app
# # import json
# # import time
# # from asgiref.sync import sync_to_async

# # class GetCart(WebsocketConsumer):
# #     @sync_to_async
# #     def get_user_by_token(self, token):
# #         print(token)
# #         print(token)
# #         print(token)
# #         print(token)
# #         print(token)
# #         print(token)
# #         print(token)
# #         print(token)
# #         print(token)
# #         print(token)
# #         print(token)
# #         print(token)
# #         print(token)
# #         print(token)
# #         print(token)
# #         return UserToken.objects.get(token=token).user

# #     async def get_from_db_to_cart(self, token):
# #         try:
# #             user = await self.get_user_by_token(token)
# #             print(user)

# #             # all_in_cards_for_this_user = await sync_to_async(
# #             #     lambda: list(CardOrderItems.objects.filter(user=user).values())
# #             # )()
# #             # 
# #             # n=0
# #             # for item in all_in_cards_for_this_user:
# #             #     card_order_item = await sync_to_async(CardOrderItems.objects.get)(id=item.get("id"))
# #             #     item["product_name"] = card_order_item.uoc_prod.title
# #             #     try:
# #             #         item["default_image"] = card_order_item.uoc_prod.image.url
# #             #     except CardOrderItems.DoesNotExist:
# #             #         item["default_image"] = None
# #             # print(all_in_cards_for_this_user)

# #             # return JsonResponse({'success': all_in_cards_for_this_user}, status=200)
# #         except Exception as e:
# #             print(e)
# #     def connect(self):
# #         user_token = self.scope['cookies'].get('user_token')

# #         self.room_group_name = None

# #         if user_token:
# #             user_token_exists = UserToken.objects.filter(token=user_token).exists()

# #             if user_token_exists:
# #                 self.room_group_name = user_token

# #                 async_to_sync(self.channel_layer.group_add)(
# #                     self.room_group_name,
# #                     self.channel_name
# #                 )

# #                 self.accept()
# #                 print(f"User token connected: {user_token}")
# #                 self.get_user_by_token(user_token)
# #                 self.send_cart_data()  # Start sending cart data

# #             else:
# #                 self.close()
# #         else:
# #             self.close()

# #     def disconnect(self, close_code):
# #         if self.room_group_name:
# #             async_to_sync(self.channel_layer.group_discard)(
# #                 self.room_group_name,
# #                 self.channel_name
# #             )

# #     def receive(self, text_data=None, bytes_data=None):
# #         data = json.loads(text_data)
# #         print(f"Received message: {data}")

# #     def send_cart_data(self):
# #         json_data = {"user_Cart": "data"}
        
# #         while True:
# #             try:
# #                 json_str = json.dumps(json_data)
                
# #                 # Replace this with your actual sending logic
# #                 self.send(json_str)
                
# #                 time.sleep(2)  # Wait for 2 seconds before sending the next message
                
# #             except Exception as e:
# #                 print(f"Error sending message: {e}")
# #                 break  # Exit the loop on error or close flag
