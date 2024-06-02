from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

class UserRegisterForms(UserCreationForm):
    username = forms.CharField(label="First & Second Name", widget=forms.TextInput(attrs={"placeholder": "Your First & Second Name", "style": "height: 50px; background-color: white; border: 1px solid aqua; width: 98%; box-sizing: border-box; color: black;"}))
    email = forms.CharField(label="E-mail", widget=forms.TextInput(attrs={" placeholder": "Email", "name":"email","style": "height: 50px; background-color: white; border: 1px solid aqua; width: 98%;   box-sizing: border-box; color: black;"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder": "Password","name":"password1","style": "height: 50px; background-color: white; border: 1px solid aqua; width: 98%;   box-sizing: border-box; color: black;" }))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password", "style": "height: 50px; background-color: white; border: 1px solid aqua; width: 98%;   box-sizing: border-box; color: black;"}))

    profile_picture = forms.ImageField(label="Profile Picture", required=True)  # Form field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForms, self).__init__(*args, **kwargs)
        self.fields['profile_picture'].widget.attrs.update({'id': 'fileInput', 'style': 'display: none;'})
