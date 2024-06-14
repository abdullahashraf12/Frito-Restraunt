from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from userauths.models import UserToken  # Assuming UserToken model is defined in your app
import json
import time

class GetCart(WebsocketConsumer):

    def connect(self):
        user_token = self.scope['cookies'].get('user_token')

        self.room_group_name = None

        if user_token:
            user_token_exists = UserToken.objects.filter(token=user_token).exists()

            if user_token_exists:
                self.room_group_name = user_token

                async_to_sync(self.channel_layer.group_add)(
                    self.room_group_name,
                    self.channel_name
                )

                self.accept()
                self.send_cart_data()  # Start sending cart data
                print(f"User token connected: {user_token}")
            else:
                self.close()
        else:
            self.close()

    def disconnect(self, close_code):
        if self.room_group_name:
            async_to_sync(self.channel_layer.group_discard)(
                self.room_group_name,
                self.channel_name
            )

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        print(f"Received message: {data}")

    def send_cart_data(self):
        json_data = {"user_Cart": "data"}
        
        while True:
            try:
                json_str = json.dumps(json_data)
                
                # Replace this with your actual sending logic
                self.send(json_str)
                
                time.sleep(2)  # Wait for 2 seconds before sending the next message
                
            except Exception as e:
                print(f"Error sending message: {e}")
                break  # Exit the loop on error or close flag

# from channels.generic.websocket import WebsocketConsumer
# from asgiref.sync import async_to_sync
# from userauths.models import UserToken  # Assuming UserToken model is defined in your app
# import json
# import asyncio

# class GetCart(WebsocketConsumer):

#     def connect(self):
#         user_token = self.scope['cookies'].get('user_token')
#         print(user_token)
#         print(user_token)
#         print(user_token)

#         self.room_group_name = None  # Initialize room_group_name

#         # Extract the user_token from headers
#         # for name, value in headers:
#         #     if name == b'user_token':
#         #         token = value.decode('utf-8')
#         #         break

#         if user_token:
#             user_token_exists = UserToken.objects.filter(token=user_token).exists()
#             print(user_token_exists)
#             if user_token_exists:
#                 self.room_group_name = user_token

#                 # Add the consumer to the room group
#                 async_to_sync(self.channel_layer.group_add)(
#                     self.room_group_name,
#                     self.channel_name
#                 )

#                 # Accept the WebSocket connection
#                 self.accept()
#                 self.send()
#                 # Print the user_token for debugging
#                 print(f"User token connected: {user_token}")
#             else:
#                 self.close()
#         else:
#             self.close()

#     def disconnect(self, close_code):
#         if self.room_group_name:
#             # Remove the consumer from the room group
#             async_to_sync(self.channel_layer.group_discard)(
#                 self.room_group_name,
#                 self.channel_name
#             )

#     def receive(self, text_data=None, bytes_data=None):
#         # Handle incoming WebSocket messages
#         data = json.loads(text_data)

#         print(f"Received message: {data}")

#     async def send(self, text_data=None, bytes_data=None, close=False):
#         return self.my_custom_send(self, text_data=None, bytes_data=None, close=False)
#     async def my_custom_send(self, text_data=None, bytes_data=None, close=False):
#         json_data = {"user_Cart": "data"}
        
#         while True:
#             try:
#                 # Convert dictionary to JSON string
#                 json_str = json.dumps(json_data)
                
#                 # Replace this with your actual sending logic
#                 # For example, if you have self.send_text(text_data) method:
#                 await self.send(json_str)
                
#                 # Wait for 2 seconds before sending the next message
#                 await asyncio.sleep(2)
                
#             except Exception as e:
#                 print(f"Error sending message: {e}")
#                 break  # Exit the loop on error or close flag