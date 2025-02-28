from userauths.models import User ,UserToken
from product.models import Category,Offers,Products
def default(request):
    category = Category.objects.all().order_by('title')
    offers = Offers.objects.all().order_by('product_offers')
    all_products_featured = Products.objects.filter(featured=True)

    if request.user.is_authenticated:
        print(request.user.profile_picture == "")
        get_token = list(UserToken.objects.filter(user=request.user).values("token"))
        get_token = get_token[0].get("token")

        if request.user.profile_picture != "":
    
            image = request.user.profile_picture.url
            return {
                    "prof_img":image,
                    "categ": category,
                    "offers":offers,
                    "all_products_featured":all_products_featured,
                    "user_token":get_token
                }
        else:
            return{
                    "categ": category,
                    "offers":offers,
                    "all_products_featured":all_products_featured ,
                    "user_token":get_token

            }
    else:
            return {
                 
                    "categ": category,
                    "offers":offers,
                    "all_products_featured":all_products_featured
            }