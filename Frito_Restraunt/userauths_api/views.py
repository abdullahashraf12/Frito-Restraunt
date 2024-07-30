from django.shortcuts import render
from django.http import JsonResponse
from userauths.models import User, UserToken
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt
from django.contrib.auth import authenticate
# Create your views here.
from django.middleware.csrf import get_token
from django.db.utils import IntegrityError
def signup(request):
    print("csrf")
    try:
        if request.method == 'POST':
            print(request)
            username = request.POST.get("username", "")
            account = request.POST.get("account", "")
            password = request.POST.get("password", "")
            bio = request.POST.get("bio", "")
            address = request.POST.get("Address", "")
            mobile_number = request.POST.get("mobile_Number", "")
            
            # Handle the profile picture upload
            if 'profilePicture' in request.FILES:
                profile_picture = request.FILES['profilePicture']
            else:
                return JsonResponse({'error': 'No profile picture found in request'}, status=400)
            
            # Check if user already exists
            user_exists = User.objects.filter(email=account, username=username).exists()
            if not user_exists:
                # Create user instance
                user = User(
                    username=username,
                    email=account,
                    password=password,
                    bio=bio,
                    Address=address,
                    mobile_Number=mobile_number,
                    profile_picture=profile_picture  # Assign profile_picture here
                )
                # Save the user instance
                user.save()
                return JsonResponse({'message': 'User created successfully'})
            else:
                return JsonResponse({'error': 'User with this email and username already exists'}, status=400)
        else:
            return JsonResponse({'error': 'Only POST requests are allowed'}, status=400)
    except IntegrityError:
        return JsonResponse({'error': 'User Already Exist'}, status=400)



def login(request):
    if request.method == 'POST':
        account = request.POST.get("account", "")
        password = request.POST.get("password", "")

        # Check if user with given account (email) exists
        try:
            user = User.objects.get(email=account)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Account does not exist'}, status=404)

        # Authenticate user
        user = authenticate(email=account, password=password)

        if user is not None:
            # User authenticated, return user token or any other necessary data
            user = User.objects.get(email=account)
            token= UserToken.objects.get(user=user)
            print(token.token)
            return JsonResponse({'message': 'Login successful', 'user_token': token.token,"image":user.profile_picture.url,'username':user.username})
        else:
            # Authentication failed (password incorrect)
            return JsonResponse({'error': 'Password incorrect'}, status=401)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=400)

def get_csrf_token(request):
    csrf = get_token(request)
    # print(csrf)
    return JsonResponse({"token":csrf})