from django.shortcuts import render

# Create your views here.
from django.shortcuts import render ,redirect
from rest_framework.response import Response
from product.models import Products,Category,CardOrder,CardOrderItems,ProductImages,ProductReview,WishList,Address,Tags,UserOrderCard,WishList,ProductReview,ProductMealType,ProductSideDish,ProdutsAdditions,Offers , ProductsOffers,OffersNames ,CashierTable
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q
from django.core.serializers import serialize
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.db.models import Sum
from django.db.models import F
from django.db import models
from django.utils import timezone
from django.http import JsonResponse, HttpResponseNotAllowed
from userauths.models import User,UserToken
from django.shortcuts import get_object_or_404
from redis.exceptions import TimeoutError ,ConnectionError




def contact_us(request):
    return render(request,"contact_us.html")








def save_cashier_table(request, id):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Retrieve the CashierTable instance
        cashier_instance = get_object_or_404(CashierTable, pk=id)
        
        # Extract data from POST request
        client_status = request.POST.get('client_status')
        sales_rep_id = request.POST.get('SalesRep')
        
        # Update instance fields based on conditions
        if sales_rep_id:
            # Convert sales_rep_id to integer if not empty
            try:
                sales_rep = User.objects.get(id=int(sales_rep_id))
                cashier_instance.SalesRep = sales_rep
            except (ValueError, User.DoesNotExist):
                return JsonResponse({'error': 'Invalid SalesRep ID'}, status=400)
        
        # Always update client_status
        cashier_instance.client_status = client_status
        
        # Save the updated instance
        cashier_instance.save()
        
        # Return updated data as JSON response
        return JsonResponse({
            'client_status': cashier_instance.client_status,
            'SalesRep': cashier_instance.SalesRep.username if cashier_instance.SalesRep else '',
        })
    else:
        # Handle other HTTP methods if necessary
        return HttpResponseNotAllowed(['POST'])







# def save_cashier_table(request, id):
#     if request.method == 'POST':
#         # Process the POST data
#         client_status = request.POST.get('client_status')
#         sales_rep = request.POST.get('SalesRep')
#         print(User.objects.get(id=int(sales_rep)))
#         print(request.user)
#         # Save the data (example: update the model instance)
#         cashier_instance = CashierTable.objects.get(pk=id)
#         cashier_instance.client_status = client_status
#         cashier_instance.SalesRep = User.objects.get(id=int(sales_rep))
#         cashier_instance.save()
#         print(cashier_instance)
#         # Return updated data as JSON response
#         return JsonResponse({
#             'client_status': cashier_instance.client_status,
#             "SalesRep":User.objects.get(id=int(sales_rep)).username
#             # 'SalesRep': cashier_instance.sales_rep,
#         })
#     else:
#         # Handle other HTTP methods if necessary
#         return HttpResponseNotAllowed(['POST'])







def user_ordered_items(request,user_email,order_number):
    print(user_email)
    print(user_email)
    print(user_email)
    print(user_email)
    print(user_email)
    print(user_email)
    print(user_email)
    get_all_from_card = CardOrderItems.objects.filter(user__email=user_email,order_number=order_number,checked_out_status=True)
    total_price = get_all_from_card.aggregate(total_price=Sum('total_price_for_all'))['total_price']
    print(order_number)
    print(total_price)
    print(get_all_from_card)
    context= {
        "my_ordered_items":get_all_from_card,
        "total_price": str(float(total_price)+50.00)
    }
    return render(request,"user_ordered_items.html",context=context)









# def user_ordered_items(request,user_email):
#     if request.user.is_authenticated and request.user.is_staff:
#         get_all_from_card = CardOrderItems.objects.filter(user__email=user_email,checked_out_status=True)
#         total_price = get_all_from_card.aggregate(total_price=Sum('total_price_for_all'))['total_price']
#         print("open headers")
#         print(request.headers.get('X-Requested-With'))
#         print(total_price)
#         print(total_price)
#         print(total_price)
#         print(total_price)
#         print(request.headers.get('X-Requested-With'))
#         print("close headers")
#         if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#             print(get_all_from_card)
#             if(total_price==None) :
#                 total_price = 0.00
                        
#             data = {
#                 "items": list(get_all_from_card.annotate(
#                     image_url=F('uoc_prod__image')
#                 ).values(
#                     'uoc_prod__title', 'image_url', 'user_meal_type', 'quantity',
#                     'MealType', 'MealSideDishes', 'MealAdditions', 'total_price_for_all'
#                 )),
#                 "total_price": float(total_price)
#                 }
            
#             print(list(data.values()))
#             print(list(data.values()))
#             print(list(data.values()))
            
#             return JsonResponse(data)

#         return render(request, "checkout.html", context={"all_from_Card": get_all_from_card, "total_price": total_price})

#     else:
#         return render(request, "checkout.html", context={})































# Create your views here.
def place_order(request):
    if request.user.is_authenticated :

#  "total_price": total_price
        if request.method == 'POST' :
            try:
                max_order_number = CashierTable.objects.aggregate(models.Max('order_number'))['order_number__max']

                # If max_order_number is None or 0, set next_order_number to 1; otherwise, increment max_order_number by 1
                next_order_number = 1 if max_order_number is None or max_order_number == 0 else max_order_number + 1

                # Update CardOrderItems for the current user where order_number is 0
                get_Card = CardOrderItems.objects.filter(user=request.user,order_number=0)
                get_Card.update(checked_out_status=True, order_number=next_order_number)
                # get_Card.delete()
                address = request.POST.get("address_1")
                print("address",address)
                client_number= request.POST.get("mobile_number")
                latitude = request.POST.get("latitude","")
                longitude= request.POST.get("longitude","")


                # ['total_sum']
                get_Card =  CardOrderItems.objects.filter(user=request.user,order_number=next_order_number)
                aggregated_result = get_Card.aggregate(total_sum=Sum('total_price_for_all'))
                print(get_Card)
                print(get_Card)
                print(get_Card)
                print(get_Card)
                print(get_Card)
                # Extract the aggregated value from the result
                total_price = aggregated_result['total_sum'] if aggregated_result['total_sum'] else 0

                # Add 50 for cashier
                total_price_with_cashier = total_price + 50
                # +50
                print(total_price_with_cashier)
                print(total_price_with_cashier)
                print(total_price_with_cashier)
                casheir = CashierTable(order_number=next_order_number,order_date=timezone.now().isoformat(),client=request.user,address=address,client_number=client_number,total_price=total_price_with_cashier,latitude=latitude,longitude=longitude)
                casheir.save()
                return redirect("core:my_orders")
            except (TimeoutError, ConnectionError):
                return redirect('core:my_orders')
            
        else:
            return redirect("core:checkout")

    else:
        return redirect("core:checkout")





def my_orders(request):
    if request.user.is_authenticated:
        today = timezone.now().date()
        get_all_from_card = CashierTable.objects.filter(client=request.user).exclude(client_status="Finished")

        total_price = get_all_from_card.aggregate(total_price=Sum('total_price'))['total_price']
        # Fetch CardOrderItems filtered by today's date, checked_out_status, and current user
        user_ordered_items = CardOrderItems.objects.filter(
            order_date__date=today,
            checked_out_status=True,
            user=request.user
        ).order_by('-order_date')  # Ensure to order by order_number

        # Retrieve related CashierTable entries based on order_number
        order_numbers = user_ordered_items.values_list('order_number', flat=True)
        cashier_tables = CashierTable.objects.filter(order_number__in=order_numbers)

        # Map CashierTable entries to CardOrderItems based on order_number
        cashier_table_dict = {table.order_number: table for table in cashier_tables}

        # Attach cashier_table to each CardOrderItems instance
        for item in user_ordered_items:
            item.cashier_table = cashier_table_dict.get(item.order_number)


        context = {
            "user_ordered_items": user_ordered_items,
            "total_price":total_price
        }
        return render(request, "MyOrders.html", context=context)

    else:
        return render(request, "MyOrders.html")

    
def user_checked_items(request,user):
    if request.user.is_authenticated and request.user.is_staff:
        # print(request.user.is_staff)
        # print(request.user.is_staff)
        # print(request.user.is_staff)
        # print(request.user.is_staff)
        # print(request.user.is_staff)
        # print(request.user.is_staff)
        # print(request.user.is_staff)
        # print(request.user.is_staff)
        cards_data = CardOrderItems.objects.filter(user=user)
        return render(request,"user_ordered_items.html",context={"cards_data":cards_data})


def all_users_ordered_items(request):
    cards_data = CardOrderItems.objects.all()
    return JsonResponse("all_Cards_for_All_users")








def checkout_ajax(request):
    if str(request.user) != "AnonymousUser":
        get_all_from_card = CardOrderItems.objects.filter(user=request.user,checked_out_status=False)
        total_price = get_all_from_card.aggregate(total_price=Sum('total_price_for_all'))['total_price']
        print("open headers")
        print(request.headers.get('X-Requested-With'))
        print(total_price)
        print(total_price)
        print(total_price)
        print(total_price)
        print(request.headers.get('X-Requested-With'))
        print("close headers")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            print(get_all_from_card)
            if(total_price==None) :
                total_price = 0.00
                        
            data = {
                "items": list(get_all_from_card.annotate(
                    image_url=F('uoc_prod__image')
                ).values(
                    'uoc_prod__title', 'image_url', 'user_meal_type', 'quantity',
                    'MealType', 'MealSideDishes', 'MealAdditions', 'total_price_for_all'
                )),
                "total_price": float(total_price)
                }
            
            print(list(data.values()))
            print(list(data.values()))
            print(list(data.values()))
            
            return JsonResponse(data)

        return render(request, "checkout.html", context={"all_from_Card": get_all_from_card, "total_price": total_price})

    else:
        return render(request, "checkout.html", context={})



















def checkout(request):
    if str(request.user) != "AnonymousUser":
        print("==================")
        print("==================")
        print("==================")
        print("==================")
        print("==================")
        print("==================")

        print("user is :"+ str(request.user))
        print(request.user)
        print(request.user)
        print("here 234")
        get_all_from_card=CardOrderItems.objects.filter(user=request.user,checked_out_status=False)
        print(list(get_all_from_card.values()))

        total_price = CardOrderItems.objects.filter(user=request.user,checked_out_status=False).aggregate(total_price=Sum('total_price_for_all'))['total_price']
        print("==================")
        print("Total Prices = "+str(total_price))
        if total_price ==None:
            total_price = 0.00
        return render(request,"checkout.html",context={"all_from_Card":get_all_from_card,"total_price":total_price,"total_price_for_all_with_Delivery":str(float(total_price+50.00))})

    else:
        return render(request,"checkout.html",context={})










def index(request):
    # bananas = Products.objects.all().order_by("-id")
    bananas = Products.objects.filter(products_status="published",featured=True).order_by("-id")

    context = {
        "products":bananas,
    }
    return render(request,template_name="index.html",context=context)


def extract_values_by_key(data, key):
    values = []
    for item in data:
        if key in item:
            values.append(item[key])
    return values

def add_to_cart(request):
    try:
        if request.method == 'POST' and str(request.user) != "AnonymousUser":
            prod_ven = request.POST.get("prod_ven")
            
            # print(request.user.is_staff)

            # request.user.is_superuser
            # request.user.groups.filter(name='admin').exists()
            if prod_ven == "Default":

                product_quantity = request.POST.get("prod_quantity_n")
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                print(product_quantity)
                prod_pid=request.POST.get("product_pid_to_card")
                Prod= Products.objects.get(pid=prod_pid)
                # Filter ProductsOffers directly
                default_products_offers = ProductsOffers.objects.filter(default=True, product=Prod)
                # Get the IDs of these ProductsOffers
                default_products_offers_ids = default_products_offers.values_list('id', flat=True)
                # Now filter CardOrderItems based on these ProductsOffers IDs
                data_exists = CardOrderItems.objects.filter(
                    user=request.user, 
                    uoc_prod=Prod, 
                    user_meal_type="Default",
                    product_offers=ProductsOffers.objects.get(product=Prod,default=True).product_offers,
                    checked_out_status=False
                )


                # data_exists=False

                # print(data_exists)
                # print(data_exists)
                # print(data_exists)
                # print(data_exists)
                # print(data_exists)
                # print(data_exists)
                # print(data_exists)
                # print(data_exists)
                # print(data_exists)
                # print(data_exists)
                # print(data_exists)
                # print(data_exists)
                # print(data_exists)
                # print(len(list(data_exists.values())))
                print("i am here 66")

                if len(list(data_exists.values()))==1:
                    print("i am here 55")
                    existing_object = CardOrderItems.objects.get(user=request.user, 
                    uoc_prod=Prod, 
                    user_meal_type="Default",
                    product_offers=ProductsOffers.objects.get(product=Prod,default=True).product_offers)
                    existing_object.quantity = product_quantity   # Increment the quantity by 1
                    print("i am here 100")

                    existing_object.total_price_for_meal = 0.00  # Assign total price for meal
                    print("i am here 200")

                    existing_object.total_price_for_MealSideDishes = 0.00  # Assign total price for side dishes
                    print("i am here 300")
                    existing_object.total_price_for_MealAdditions = 0.00  # Assign total price for additions
                    print("i am here 400")

                    existing_object.total_price_for_all = float(Prod.price) * float(product_quantity)   # Assign total price for all
                    print("i am here 500")

                    # existing_object.product_offers=ProductsOffers.objects.get(product=Prod,default=True)
                    existing_object.save()
                    print("i am here 77")

                    # print("hrereee")
                elif(len(list(data_exists.values()))==0):
                    
                    print(ProductsOffers.objects.get(product=Prod,default=True).product_offers.oid)
                    print(ProductsOffers.objects.get(product=Prod,default=True).product_offers.oid)
                    print(ProductsOffers.objects.get(product=Prod,default=True).product_offers.oid)
                    print(ProductsOffers.objects.get(product=Prod,default=True).product_offers.oid)
                    default_meal_type = ProductMealType.objects.filter(product=Prod, default=True)
                    default_meal_side_dishes = ProductSideDish.objects.filter(product=Prod, default=True)
                    default_meal_additions = ProdutsAdditions.objects.filter(product=Prod, default=True)
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print(list(default_meal_type.values()))
                    print(list(default_meal_side_dishes.values()))
                    print(list(default_meal_additions.values()))

                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

                    product_meal_type_ids = [meal_type.product_Meal_TYPE_id for meal_type in default_meal_type]
                    default_meal_side_dishes = [side_dish.product_SIDE_DISH_id for side_dish in default_meal_side_dishes]
                    default_meal_additions = [additions.product_additions_id for additions in default_meal_additions]
                    # meal_type = default_meal_type.value if default_meal_type else "Default"
                    # meal_side_dishes = default_meal_side_dishes.value if default_meal_side_dishes else "Default"
                    # meal_additions = default_meal_additions.value if default_meal_additions else "Default"
                 

                        


                    model=CardOrderItems(user=request.user,uoc_prod=Prod,user_meal_type="Default",quantity=product_quantity,MealType=product_meal_type_ids,MealSideDishes=default_meal_side_dishes,MealAdditions=default_meal_additions,total_price_for_meal=0.00,total_price_for_MealSideDishes=0.00,total_price_for_MealAdditions=0.00,total_price_for_all=float(Prod.price)*float(product_quantity),product_offers=ProductsOffers.objects.get(product=Prod,default=True).product_offers)
                    model.save()
                    print("i am here 88")

                    # print("hrereee 22")

                # print("Data Saved")
                return JsonResponse({'message': 'Product added to cart'})
            elif(prod_ven=="Special Order"):
                    
                pid=request.POST.get("pid")
                offer_oid=request.POST.get("offer_oid")
                print(offer_oid)
                print(offer_oid)
                print(offer_oid)
                print(offer_oid)
                print(offer_oid)
                print(offer_oid)
                print(offer_oid)
                print(offer_oid)
                print(offer_oid)
                print(offer_oid)
                Prod= Products.objects.get(pid=pid)
                print("222222222222222222222")
                data_exists = CardOrderItems.objects.filter(user=request.user, uoc_prod=Prod, user_meal_type="Special Order",checked_out_status=False).exists()
                print("444444444444444444444444")

                mealType = request.POST.get("mealType")
                sideDishtype = request.POST.get("sideDishtype")
                prductAdditionstype = request.POST.get("prductAdditionstype")
                mealType = json.loads(mealType)
                sideDishtype = json.loads(sideDishtype)
                prductAdditionstype = json.loads(prductAdditionstype)
                print(mealType)
                print(mealType)
                print(mealType)
                print(mealType)
                # print(extract_values_by_key(mealType,"product_meal_type"))
                # print(pid)
                # print(mealType)
                # print(sideDishtype)
                # print(prductAdditionstype)
                mealtype_data = "["
                product_side_dish="["
                additionName="["
                total_price=0
                total_price_for_meal=0.00
                total_price_for_MealSideDishes=0.00
                total_price_for_MealAdditions=0.00
                total_for_total=0.00
                for i in mealType:
                    name_meal = i.get("product_meal_type")
                    meal_Quatity = i.get("quantity")
                    total_price+= float(i.get("price"))
                    total_price_for_meal+=float(i.get("price")) * float(meal_Quatity)
                    # print(name_meal)
                    # print(meal_Quatity)
                    mealtype_data += name_meal + ":" + meal_Quatity + " , "  # Add each meal data to mealtype_data

                if mealtype_data.endswith(", "):  # Remove the last comma and space if present
                    mealtype_data = mealtype_data[:-2]

                mealtype_data += "]"  # Add closing bracket to mealtype_data
                # print(mealtype_data)


                for i in sideDishtype:
                    side_dish = i.get("product_side_dish")
                    side_dish_Quatity = i.get("quantity")
                    total_price+= float(i.get("price"))
                    total_price_for_MealSideDishes+=float(i.get("price")) * float(side_dish_Quatity)

                    # print(name_meal)
                    # print(meal_Quatity)
                    product_side_dish += side_dish + ":" + side_dish_Quatity + " , "  # Add each meal data to mealtype_data

                if product_side_dish.endswith(", "):  # Remove the last comma and space if present
                    product_side_dish = product_side_dish[:-2]

                product_side_dish += "]"  # Add closing bracket to mealtype_data
                # print(product_side_dish)




                for i in prductAdditionstype:
                    additionName_value = i.get("additionName")
                    additionName_quantity = i.get("quantity")
                    total_price+= float(i.get("price"))

                    # print(additionName_value)
                    # print(additionName_quantity)
                    additionName += additionName_value + ":" + additionName_quantity + " , "  # Add each addition data to additionName
                    total_price_for_MealAdditions+=float(i.get("price")) * float(additionName_quantity)
                # print("-------------------------------------")
                # print(total_price_for_MealAdditions)
                # print("-------------------------------------")
                
                if additionName.endswith(", "):  # Remove the last comma and space if present
                    additionName = additionName[:-2]

                additionName += "]"  # Add closing bracket to additionName
                # print(additionName)
                # print(total_price)


                total_for_total = total_price_for_meal + total_price_for_MealSideDishes + total_price_for_MealAdditions
                # print("------------------Total-------------------")
                # print(total_for_total)
                # print("-------------------------------------")
                if data_exists == False:
                        model=CardOrderItems(user=request.user,uoc_prod=Prod,user_meal_type="Special Order",quantity=0,MealType=mealType,MealSideDishes=sideDishtype,MealAdditions=prductAdditionstype,total_price_for_meal=total_price_for_meal,total_price_for_MealSideDishes=total_price_for_MealSideDishes,total_price_for_MealAdditions=total_price_for_MealAdditions,total_price_for_all=total_for_total,product_offers= Offers.objects.get(oid=offer_oid))
                        # model=CardOrderItems(user=request.user,uoc_prod=Prod,user_meal_type="Special Order",Product_Quantity_IF_Default=0,MealType=mealType,MealSideDishes=sideDishtype,MealAdditions=prductAdditionstype)

                        model.save()
                else:
                        print("90909909")
                        try:
                            existing_object=CardOrderItems.objects.get(user=request.user, uoc_prod=Prod, user_meal_type="Special Order",product_offers= Offers.objects.get(oid=offer_oid),checked_out_status=False)
                            print("58585885855")

                            existing_object.quantity = 0  
                            existing_object.total_price_for_meal =total_price_for_meal  
                            existing_object.total_price_for_MealSideDishes =total_price_for_MealSideDishes  # Assign total price for side dishes
                            existing_object.total_price_for_MealAdditions = total_price_for_MealAdditions  # Assign total price for additions
                            existing_object.MealType=mealType
                            existing_object.MealSideDishes=sideDishtype
                            existing_object.MealAdditions=prductAdditionstype
                            existing_object.total_price_for_all = total_for_total  # Assign total price for all
                            existing_object.product_offers = Offers.objects.get(oid=offer_oid)  # Assign total price for all

                            existing_object.save()
                        except Exception as e:
                            model=CardOrderItems(user=request.user,uoc_prod=Prod,user_meal_type="Special Order",quantity=0,MealType=mealType,MealSideDishes=sideDishtype,MealAdditions=prductAdditionstype,total_price_for_meal=total_price_for_meal,total_price_for_MealSideDishes=total_price_for_MealSideDishes,total_price_for_MealAdditions=total_price_for_MealAdditions,total_price_for_all=total_for_total,product_offers= Offers.objects.get(oid=offer_oid))

                            model.save()
                        # MealType=mealtype_data,MealSideDishes=product_side_dish,MealAdditions=additionName,total_price_for_meal=total_price_for_meal,total_price_for_MealSideDishes=total_price_for_MealSideDishes,total_price_for_MealAdditions=total_price_for_MealAdditions,total_price_for_all=total_price)
                        
                return JsonResponse({'Success': 'Ajax Has Been Sent'}, status=200)
            else:
                return JsonResponse({'error': 'Invalid value for prod_ven'}, status=200)
        elif request.method == 'POST' and str(request.user) == "AnonymousUser":
            return JsonResponse({'error': 'User Must Login To Add To Card'}, status=200)
        elif request.method == 'GET' and request.user =="AnonymousUser":
            return JsonResponse({'error': 'User Must Login To Add To Card'}, status=200)
        elif request.method == 'GET' and request.user != "AnonymousUser":
            user = request.user
            all_in_cards_for_this_user = list(CardOrderItems.objects.filter(user=user,checked_out_status=False).values())

            print("++++++++++++++++++++++++++++++")
            print(all_in_cards_for_this_user)
            print(all_in_cards_for_this_user)
            print("++++++++++++++++++++++++++++++")

            # data = []
            n=0
            for item in all_in_cards_for_this_user:
                card_order_item = CardOrderItems.objects.get(id=item.get("id"),checked_out_status=False)

                item["product_name"] = card_order_item.uoc_prod.title
                try:
                    item["default_image"] = card_order_item.uoc_prod.image.url
                except CardOrderItems.DoesNotExist:
                    # Handle the case where the CardOrderItems object doesn't exist
                    item["default_image"] = None  # or any default image URL you want to assign
            print(all_in_cards_for_this_user)
                # print(item.get("id"))
                # product_name=CardOrderItems.objects.get(id=item.get("id")).uoc_prod.title
                # print(product_name)
                # print(item.get("uoc_prod_id"))
                # n+=1
                # item_data = {
                    # 'uoc_prod': item.uoc_prod.title,  # Retrieve the title from Products model
            #         'user_meal_type': item.user_meal_type,
            #         'quantity': item.quantity,
            #         'MealType': item.MealType,
            #         'MealSideDishes': item.MealSideDishes,
            #         'MealAdditions': item.MealAdditions,
            #         'total_price_for_meal': item.total_price_for_meal,
            #         'total_price_for_MealSideDishes': item.total_price_for_MealSideDishes,
            #         'total_price_for_MealAdditions': item.total_price_for_MealAdditions,
            #         'total_price_for_all': item.total_price_for_all
                # }
            print()
            
            #     data.append(item_data)
            return JsonResponse({'success': all_in_cards_for_this_user}, status=200)

    except Exception as er:
        print(request.user)
        if(str(request.user) == "AnonymousUser"):
            return JsonResponse({'error': 'User Empty'}, status=200)
        else:
            print(er)
            return JsonResponse({'error': 'Invalid Request'}, status=200)






















def remove_from_Card(request):
    if request.user:
        user=request.user
        product_id_remove_from_button=request.POST.get("product_id_remove_from_button")
        product_type_def_special=request.POST.get("product_type_def_special")
        offer_type=request.POST.get("offer_type")
        # add product_offer
        print(offer_type)
        print(offer_type)
        print(offer_type)
        print(offer_type)
        print(offer_type)
        print(offer_type)
        print(offer_type)

        get_from_Card_by_user_and_product_id = None
        print(product_id_remove_from_button)
        print(product_type_def_special)
        try:
            get_from_Card_by_user_and_product_id = CardOrderItems.objects.get(user=user, uoc_prod=product_id_remove_from_button,user_meal_type=product_type_def_special,product_offers= Offers.objects.get(product_offers= OffersNames.objects.get(product_offers_offers=offer_type)),checked_out_status=False  )
        except CardOrderItems.DoesNotExist:
            pass

        if get_from_Card_by_user_and_product_id:
            get_from_Card_by_user_and_product_id.delete()
            return JsonResponse({"sucess":"Product Removes"})

        else:
            return JsonResponse({"error":"Product Not Exists"})
    else:
        return JsonResponse({"error":"user Not Logged In"})








def product_list(request):
    bananas = Products.objects.filter(products_status="published",featured=True).order_by("-id")
    context = {
        "products":bananas
    }
    return render(request,template_name="shop-filter.html",context=context)

def category_list(request):
    bananas_category = Category.objects.all()

    context = {
        "category":bananas_category
    }
    return render(request,template_name="blog-category-list.html",context=context)
def category_product_list_view(request,cid):
    category = Category.objects.get(cid=cid)  # Retrieve a single Category object
    products = Products.objects.filter(products_status="published",category=category)
    categ_all = Category.objects.all()
    context={
        "category":category,
        "products":products,
        "categ_all":categ_all
    }
    return render(request=request,template_name="shop-grid-left.html",context=context)


# def offers_product_list_view(request, oid):
#     offer = get_object_or_404(Offers, oid=oid)
#     # Filter products that are associated with the given offer and have a status of "published"
#     products = Products.objects.filter(products_status="published", ProductsOffers__product_offers=offer)
#     # categ_all = Category.objects.all()
    
#     context = {
#         "products": products,
#         "offer": offer
#     }
#     return render(request=request, template_name="shop-offer.html", context=context)


def offers_product_list_view(request,oid):
    offer = Offers.objects.get(oid=oid)
    print(offer)
    products = Products.objects.filter(products_status="published", Products_Offers_prod__product_offers=offer)
    
    categ_all = Category.objects.all()
    context={
        "products":products,
        "categ_all":categ_all
    }
    return render(request=request,template_name="shop-offer.html",context=context)













# def show_vendor_list(request):
#     vendor  = Vendor.objects.all()
#     context = {
#         "vendors":vendor
#     }
#     return render(request=request,template_name="vendors-list.html",context=context)

# def vendor_details_view(request,vid):
#     vendor  = Vendor.objects.get(vid=vid)
#     products=Products.objects.filter(vendor=vendor,products_status="published")
#     category = Category.objects.all()

#     context = {
#         # "vendor":vendor,
#         "products":products,
#         "category":category

#     }
#     return render(request=request,template_name="vendor-details-2.html",context=context)

def get_product_by_id(request, pid):
    # Get the product object
    product=Products.objects.get(pid=pid)

    p_images = product.p_images.all()
    related_products = Products.objects.filter(category=product.category).exclude(pid=pid)
    category = Category.objects.all()
    latest_products = Products.objects.filter(category=product.category).exclude(pid=pid).order_by('date')
    ProductMealType = product.ProductMealTYPE.all()
    ProductSideDish = product.ProductSideDish.all()
    ProdutsAdditions = product.ProdutsAdditions.all()
    product_offer_not_default=None
    # Fetch the related offer details
    try:
        product_offer = ProductsOffers.objects.get(product=product, default=True)
        product_offer_not_default = ProductsOffers.objects.filter(product=product)

        offer_image = product_offer.product_offers.offer_image.url
        offer_name = product_offer.product_offers.product_offers.product_offers 
    except ProductsOffers.DoesNotExist:
        offer_image = None
        offer_name = None

    context = {
        "product": product,
        "p_images": p_images,
        "related_products": related_products,
        "category": category,
        "latest_products": latest_products,
        "ProductMealType": ProductMealType,
        "ProductSideDish": ProductSideDish,
        "ProdutsAdditions": ProdutsAdditions,
        'is_product_page': True,
        "offer_image": offer_image,
        "offer_name": offer_name,
        "all_offers":product_offer_not_default
    }
    print(related_products)
    return render(request, template_name="shop-product-vendor.html", context=context)

def get_products_name(request):
    categ_name = request.GET.get('category_category')
    prod_name = request.GET.get('search_name')
    print(categ_name)
    print(categ_name)
    print(categ_name)
    print(categ_name)

    print(prod_name)
    print(prod_name)

    print(prod_name)
    print(prod_name)

    bananas = Products.objects.all()
    tags = Tags.objects.all()
    if(categ_name=="All Categories" or categ_name==""):
        bananas = Products.objects.filter(products_status="published",title__icontains=prod_name)
        print(categ_name)
        print(prod_name)
        print(bananas.count())
        print("I am Here 1")

    else:
        bananas = Products.objects.filter(products_status="published",title__icontains=prod_name,category__cid=categ_name)
        print(categ_name)
        print(prod_name)
        print(bananas.count())
        print("I am Here 2")
    context = {
        "products":bananas,
        "tags":tags
    }
    return render(request,template_name="shop-filter.html",context=context)

def show_card(request):
    if request.user.is_authenticated:
        email = request.user.email
        user_order_cards = UserOrderCard.objects.filter(
                Q(user__email=email)
            ).select_related('uoc_prod')
        user_order_cards_data = user_order_cards.values(
            
                'uoc_prod__title',
                'uoc_prod__price',
                'uoc_prod__image',
                'uoc_prod__pid',
                'qty',
                'weight'
            )
        context={
            "client_card":user_order_cards_data
            }
        return render(request, template_name="shop-cart.html",context=context)
    else:
        return redirect("userauths:sign-in")





class AddToCardView(APIView):
    def add_to_card_post(self, request):
        pid = request.data.get('pid')
        qty = request.data.get('qty')
        size = request.data.get('size')
        try:
            email = request.user.email
            pid = request.data.get('pid')
            qty = request.data.get('qty')
            size = request.data.get('size')
            print("i am here 1")
            # Assuming 'pid' is unique for products, you may need to handle multiple instances if not unique
            user_order_cards = UserOrderCard.objects.filter(
                Q(user__email=email) & Q(uoc_prod__pid=pid)
            )
           

            if user_order_cards.exists():
                # Update the quantity and size fields of existing UserOrderCard instances
                for user_order_card in user_order_cards:
                    user_order_card.qty = qty
                    user_order_card.weight = size
                    user_order_card.save()

                # Assuming you only want to return the uoc_id of the first matching UserOrderCard instance
                uoc_id = user_order_cards.first().uoc_id
                return Response({"prod_card": uoc_id})
            else:
                print("i am here 44")

                if qty is not None or qty != "": 
                    print("i am here 33")
                    
                    # Ensure qty is not None before creating the UserOrderCard instance
                    card = UserOrderCard(user=request.user, uoc_prod=Products.objects.get(pid=pid), qty=qty, weight=size)
                    card.save()
                    return Response({"message": "No matching product in the user's order card."})
                
                else:
                    print("i am here 22")
                    print(pid)
                    print(qty)
                    print(size)
                    return Response({"error": "Quantity cannot be empty."}, status=400)
        except Exception as e:
            print(pid)
            print(qty)
            print(size)
            print("i am here 2 ")
            print(e)
            return Response({"error": str(e)}, status=400)
    def add_to_card_get(self, request):
        try:
            email = request.user.email
            user_order_cards_all = UserOrderCard.objects.filter(
                user__email=email
            )
            
            # Select specific fields from the related Products model
            user_order_cards_all = user_order_cards_all.select_related('uoc_prod')
            user_order_cards_data = user_order_cards_all.values(
                'uoc_id',
                'user__email',
                'uoc_prod__title',
                'uoc_prod__price',
                'uoc_prod__image',
                'uoc_prod__pid',
                'qty',
                'weight'
            )
            
            # Convert the values queryset to a list of dictionaries
            user_order_cards_list = list(user_order_cards_data)
            
            # Use JSON encoder to serialize the list of dictionaries
            serialized_data = json.dumps(user_order_cards_list, cls=DjangoJSONEncoder)
            
            return JsonResponse({"prod_card": serialized_data}, safe=False)
        except Exception as e:
            return JsonResponse({"prod_card": ""}, safe=False)

    def get(self, request, *args, **kwargs):
        return self.add_to_card_get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.add_to_card_post(request, *args, **kwargs)

class RemoveFromCardView(APIView):
    def remove_card_post(self, request):
        try:
            email = request.user.email
            pid = request.data.get('pid')
            
            # Assuming 'pid' is unique for products, you may need to handle multiple instances if not unique
            user_order_cards = UserOrderCard.objects.filter(
                Q(user__email=email) & Q(uoc_prod__pid=pid)
            )
            
            if user_order_cards.exists():
                user_order_cards.delete()
                prod_Delete_stat = "Success"
                return Response({"Product_Delete_Status": prod_Delete_stat})
            else:
                prod_Delete_stat = "Failed"
                return Response({"Product_Delete_Status": prod_Delete_stat + " Product Is Not In The Cart"})
                
        except Exception as e:
            return Response({"error": str(e)}, status=400)
        
    def post(self, request, *args, **kwargs):
        return self.remove_card_post(request, *args, **kwargs)
 
















class RemoveFromWishCardView(APIView):
    def remove_wishcard_post(self, request):
        try:
            email = request.user.email
            pid = request.data.get('pid')
            print("Removing In Progress")

            # Assuming 'pid' is unique for products, you may need to handle multiple instances if not unique
            user_order_cards = WishList.objects.filter(
                Q(user__email=email) & Q(product__pid=pid)
            )
            if user_order_cards.exists():
                user_order_cards.delete()
                prod_Delete_stat = "Success"
                print("items should be removed")

                return Response({"Product_Delete_Status": prod_Delete_stat})
            else:
                prod_Delete_stat = "Failed"
                return Response({"Product_Delete_Status": prod_Delete_stat + " Product Is Not In The Cart"})
                
        except Exception as e:
            return Response({"error": str(e)}, status=400)
        
    def post(self, request, *args, **kwargs):
        return self.remove_wishcard_post(request, *args, **kwargs)







class AddReview(APIView):
    def post(self, request, *args, **kwargs):
        return self.postAddReview(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.getReview(request, *args, **kwargs)

    def postAddReview(self, request):
        try:
            email = request.user.email
            pid = request.data.get('pid')
            starRating = request.data.get("stars")
            user_comment= request.data.get("comment")
            checkReviewExist = ProductReview.objects.filter(
                Q(user__email=email) & Q(product__pid=pid)
            )
            if checkReviewExist.exists():
                return Response({"Error": "You Already Commented"})
            else:
                new_review = ProductReview.objects.create(
                    user=request.user,
                    product=Products.objects.get(pid=pid),
                    review=user_comment,
                    rating=starRating
                )
                return Response({"commentSaved": "Commented Successfully"})
        except Exception as e:
            print(e)
            return Response({"error": str(e)}, status=400) 

    def getReview(self, request):
        try:
            pid = request.GET.get('pid')
            product = Products.objects.get(pid=pid)
            user_order_cards_all = ProductReview.objects.filter(
                product__pid=pid
            )
            review_data = user_order_cards_all.values(
                'user__username',
                'review',
                'rating',
                'date'
            )

            max_percentage = 0
           
            
            rating_percentages = product.get_rating_percentage()
            for key, value in rating_percentages.items():
                if value > max_percentage:
                    max_percentage = value
        
            result_data = {
                "comments": list(review_data),
                "rating_percentages": rating_percentages,
                'glob_precentage':max_percentage
            }

            return JsonResponse(result_data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)





















class AddToWishCardView(APIView):
    def add_to_Wishcard_post(self, request):
        pid = request.data.get('pid')
 
        try:
            email = request.user.email
            pid = request.data.get('pid')

            print("i am here 1")
            # Assuming 'pid' is unique for products, you may need to handle multiple instances if not unique
            user_order_cards = WishList.objects.filter(
                Q(user__email=email) & Q(product__pid=pid)
            )
           
            if user_order_cards.exists():
                # Update the quantity and size fields of existing UserOrderCard instances
                # for user_order_card in user_order_cards:
                #     user_order_card.save()

                # # Assuming you only want to return the uoc_id of the first matching UserOrderCard instance
                # uoc_id = user_order_cards.first().id
                print(pid)
                return Response({"prod_card": "Product Already Exists"})
            else:
                    card = WishList(user=request.user, product=Products.objects.get(pid=pid))
                    card.save()
                    return Response({"message": "Product Added Sucessfully"})
               
        except Exception as e:
            print(pid)

            print("i am here 2 ")
            print(e)
            return Response({"error": str(e)}, status=400)
    def add_to_Wishcard_get(self, request):
        try:
            email = request.user.email
            user_order_cards_all = WishList.objects.filter(
                user__email=email
            )

            
            # Select specific fields from the related Products model
            user_order_cards_all = user_order_cards_all.select_related('product')
            print(user_order_cards_all)

            user_order_cards_data = user_order_cards_all.values(
                'id',
                'user__email',
                'product__title',
                'product__price',
                'product__image',
                'product__pid',

            )
            # Convert the values queryset to a list of dictionaries
            user_order_cards_list = list(user_order_cards_data)
            
            # Use JSON encoder to serialize the list of dictionaries
            serialized_data = json.dumps(user_order_cards_list, cls=DjangoJSONEncoder)
            
            return JsonResponse({"prod_card": serialized_data}, safe=False)
        except Exception as e:
            return JsonResponse({"prod_card": ""}, safe=False)

    def get(self, request, *args, **kwargs):
        return self.add_to_Wishcard_get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.add_to_Wishcard_post(request, *args, **kwargs)

# class WishCardView(APIView):
#     def remove_card_post(self, request):
#         try:
#             email = request.user.email
#             pid = request.data.get('pid')
            
#             # Assuming 'pid' is unique for products, you may need to handle multiple instances if not unique
#             user_order_cards = UserOrderCard.objects.filter(
#                 Q(user__email=email) & Q(uoc_prod__pid=pid)
#             )
            
#             if user_order_cards.exists():
#                 user_order_cards.delete()
#                 prod_Delete_stat = "Success"
#                 return Response({"Product_Delete_Status": prod_Delete_stat})
#             else:
#                 prod_Delete_stat = "Failed"
#                 return Response({"Product_Delete_Status": prod_Delete_stat + " Product Is Not In The Cart"})
                
#         except Exception as e:
#             return Response({"error": str(e)}, status=400)
        
#     def post(self, request, *args, **kwargs):
#         return self.remove_card_post(request, *args, **kwargs)
 



















def wishlist(request):
    if request.user.is_authenticated:
        wishlist = WishList.objects.filter(
                    Q(user__email=request.user.email)
                )
        wishlist=wishlist.select_related('product')
        context={
            "wishlist":wishlist
        }
        return render(request=request,template_name="shop-wishlist.html",context=context)
    else:
        return render(request=request,template_name="shop-wishlist.html")


# def add_to_card(request):
#     context={}
#     print(request.user.username)

#     if(request.method == "POST"):
#         # request.POST.get("")
#         data=UserOrderCard()
#         data.save()
#         context={

#         }

#         return Response(context)
#     else:
#         context={}

#         return Response(context)
def message_socket(request):
    return render(request=request,template_name="websocket_form.html")




