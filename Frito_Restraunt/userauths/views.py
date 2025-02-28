from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForms
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from bs4 import BeautifulSoup
from .models import User as us
from django.http import JsonResponse

def set_error(request, error_type, message):
    request.session[error_type] = message

def get_error(request, error_type):
    return request.session.get(error_type, "")

def clear_errors(request):
    if 'error_password' in request.session:
        del request.session['error_password']
    if 'error_account' in request.session:
        del request.session['error_account']

User = settings.AUTH_USER_MODEL

def register_or_login_user(request):
    print("here 19")
    form = UserRegisterForms()
    context = {
        "form": form,
        "error_password": get_error(request, "error_password"),
        "error_account": get_error(request, "error_account")
    }

    clear_errors(request)

    if request.user.is_authenticated:
        return redirect("home:home")

    if request.method == "POST":
        if 'action' in request.POST:
            action = request.POST['action']
            if action == 'Register':
                print("here 20")

                return register_user(request, context)
            elif action == 'Login':
                print("here 21")

                return login_view(request, context)
            else:
                print("here 22")
                return login_view(request, context)


    return render(request, "login.html", context=context)

def register_user(request, context):
    form = UserRegisterForms(request.POST, request.FILES)
    if form.is_valid():
        new_user = form.save()
        username = form.cleaned_data["username"]
        messages.success(request, f"Hey {username}, your account has been created")
        new_user = authenticate(username=form.cleaned_data["email"], password=form.cleaned_data["password1"])
        login(request, new_user)
        return redirect("home:home")
    else:
        specific_errors = []
        html_string = str(form.errors)
        soup = BeautifulSoup(html_string, 'html.parser')
        error_items = soup.find_all('ul', class_='errorlist')
        for error_item in error_items:
            error_message = error_item.find('li').text
            specific_errors.append(error_message)
            print(error_message)

        for i in specific_errors:
            if i == "The two password fields didn’t match.":
                context["error_password"] = i
                set_error(request, "error_password", i)
            elif i == "User with this Email already exists.":
                context["error_account"] = i
                set_error(request, "error_account", i)
            elif i =="The password is too similar to the username.":
                context["error_password"] = "The password is too similar to the username"
                set_error(request, "error_password", i)
            elif i=="User with this Username already exists.":
                context["error_account"] = i
                set_error(request, "error_account", i)
            elif i=="Enter a valid email address.":
                context["error_account"] = i
                set_error(request, "error_account", i)
            else:
                set_error(request, "error_account", "Error Account")
                set_error(request, "error_password", "Error Password")


        return render(request, "login.html", context=context)

def login_view(request, context):
    if request.user.is_authenticated:
        return redirect("home:home")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user_account = us.objects.get(email=email)
            user = authenticate(request=request, email=email, password=password)
            if user is not None:
                login(request=request, user=user)
                messages.success(request=request, message="You are logged in.")
                return redirect("home:home")
            else:
                context["error_password"] = "Wrong Password"
                set_error(request, "error_password", "Wrong Password")
            return redirect("userauths:login")
        except us.DoesNotExist:
            context["error_account"] = "User Not Registered"
            set_error(request, "error_account", "User Not Registered")
            return redirect("userauths:register")
        except Exception as err:
            print(err)
            set_error(request, "error_account", "An unexpected error occurred.")
            return render(request, "login.html", context=context)

    return render(request, "login.html", context=context)

def logout_view(request):
    clear_errors(request)
    logout(request)
    messages.warning(request, message="User logged out")
    return redirect("home:home")


def fetch_img(request):
    if request.method == "POST":
        email = request.POST.get("email")
        print(email)
        try:
            user = us.objects.get(email=email)
            if user.profile_picture:
                return JsonResponse({"img": user.profile_picture.url})
            else:
                print("here 1 ")

                return JsonResponse({"img": ""})
        except us.DoesNotExist:
            print("here 2 ")

            return JsonResponse({"img": ""})
    else:
        return JsonResponse({"error": "Invalid request method"})


# from django.shortcuts import render, redirect
# from userauths.forms import UserRegisterForms
# from django.contrib import messages
# from django.contrib.auth import login, authenticate , logout
# from django.conf import settings
# from bs4 import BeautifulSoup
# from .models import User as us
# class Setter_Getter:
#     def __init__(self,error_password="",error_account=""):
#         self.error_password=error_password
#         self.error_account=error_account
#     def set_error_account(self,value):
#         self.error_account=value
#     def set_error_password(self,value):
#         self.error_password=value
#     def get_error_password(self):
#         return self.error_password
#     def get_error_account(self):
#         return self.error_account

# data = Setter_Getter()
# User = settings.AUTH_USER_MODEL
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from .forms import UserRegisterForms

# def register_or_login_user(request):
#     form = UserRegisterForms()
#     context = {"form": form, "error_password": data.get_error_password(), "error_account": data.get_error_account()}
#     # if request.method == "POST":
#     #     form = UserRegisterForms(request.POST, request.FILES)
#     #     if form.is_valid():
#     #         new_user = form.save()
#     #         username = form.cleaned_data["username"]
#     #         messages.success(request, f"Hey {username}, your account has been created")
#     #         new_user = authenticate(username=form.cleaned_data["email"], password=form.cleaned_data["password1"])
#     #         login(request, new_user)
#     #         return redirect("home:home")
#     #     else:
#     #         # Handle form errors
#     #         specific_errors = []
#     #         html_string = str(form.errors)
#     #         soup = BeautifulSoup(html_string, 'html.parser')
#     #         error_items = soup.find_all('ul', class_='errorlist')
#     #         for error_item in error_items:
#     #             error_message = error_item.find('li').text
#     #             specific_errors.append(error_message)

#     #         for i in specific_errors:
#     #             if i == "The two password fields didn’t match.":
#     #                 context["error_password"] = i
#     #                 data.set_error_password(i)
#     #             elif i == "User with this Email already exists.":
#     #                 context["error_account"] = i
#     #                 data.set_error_account(i)
#     #             else:
#     #                 data.set_error_account("error Account")
#     #                 data.set_error_password("error password")

#     #         return render(request, "login.html", context=context)

#     # else:
#     if request.user.is_authenticated:
#         data.set_error_password("")
#         data.set_error_account("")
#         return redirect("home:home")
    
#     # Check if the submit button for registration or login was clicked
#     if 'action' in request.POST:
#         action = request.POST['action']
#         print(action)
#         if action == 'Register':
#             return register_user(request, context)
#         elif action == 'Login':
#             return login_view(request, context)

#     return render(request, "login.html", context=context)

# def register_user(request, context):
#     form = UserRegisterForms(request.POST, request.FILES)
#     if form.is_valid():
#         new_user = form.save()
#         username = form.cleaned_data["username"]
#         messages.success(request, f"Hey {username}, your account has been created")
#         new_user = authenticate(username=form.cleaned_data["email"], password=form.cleaned_data["password1"])
#         login(request, new_user)
#         return redirect("home:home")
#     else:
#         # Handle form errors
#         specific_errors = []
#         html_string = str(form.errors)
#         soup = BeautifulSoup(html_string, 'html.parser')
#         error_items = soup.find_all('ul', class_='errorlist')
#         for error_item in error_items:
#             error_message = error_item.find('li').text
#             specific_errors.append(error_message)

#         for i in specific_errors:
#             if i == "The two password fields didn’t match.":
#                 context["error_password"] = i
#                 data.set_error_password(i)
#             elif i == "User with this Email already exists.":
#                 context["error_account"] = i
#                 data.set_error_account(i)
#             else:
#                 data.set_error_account("error Account")
#                 data.set_error_password("error password")

#         return render(request, "login.html", context=context)

# def login_view(request, context):
#     context={"error_password": data.get_error_password(), "error_account": data.get_error_account()}
#     if request.user.is_authenticated:
#         return redirect("home:home")
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         try:
#             user_account = us.objects.get(email=email)
#             print(user_account)
#             print(user_account)
#             print(user_account)
#             user = authenticate(request=request, email=email, password=password)
#             if user is not None:
#                 login(request=request, user=user)
#                 messages.success(request=request, message="You Are Logged in.")
#                 return redirect("home:home")
#             elif(user is None and user_account!=None or user_account=="" ):
#                 context["error_password"]=="Wrong Password"
#                 data.set_error_password("Wrong Password")
#                 return redirect("userauths:login")


#         except Exception as err:
#             print(err)
#             if(str(err) == "User matching query does not exist." ):
#                 print("true user doesn't exist")
#                 data.set_error_account("User Not Registred")
#                 return redirect("userauths:register")


#     return render(request, "login.html", context=context)








































# def logout_view(request):
#     data.set_error_password("")
#     data.set_error_account("")
#     logout(request)
#     messages.warning(request,message="User Logout")
#     return redirect("home:home")
