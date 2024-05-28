from userauths.models import User
def default(request):
    if request.user.is_authenticated:
        print(request.user.profile_picture == "")
        if request.user.profile_picture != "":
    
            image = request.user.profile_picture.url
            return {
                    "prof_img":image
                }
        else:
            return{

            }
    else:
            return {}