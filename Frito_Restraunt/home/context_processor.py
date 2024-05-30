from userauths.models import User
from product.models import Category
def default(request):
    category = Category.objects.all().order_by('title')

    if request.user.is_authenticated:
        print(request.user.profile_picture == "")
        if request.user.profile_picture != "":
    
            image = request.user.profile_picture.url
            return {
                    "prof_img":image,
                    "categ": category
                }
        else:
            return{
                    "categ": category
            }
    else:
            return {
                 
                    "categ": category
            }