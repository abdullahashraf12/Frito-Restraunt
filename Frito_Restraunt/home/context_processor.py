from userauths.models import User
def default(request):
    if request.user.is_authenticated:
        image = request.user.profile_picture.url
        return {
                "prof_img":image
            }
    else:
        return {}