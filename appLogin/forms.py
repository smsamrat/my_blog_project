from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from django.contrib.auth.models import User 
from  appLogin.models import UserProfiles 

class signUpForm(UserCreationForm):
    email = forms.EmailField(label='email address', required=True)
    class Meta:
        model = User
        fields= ('username','email','password1','password2')

class userchangedProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email','first_name', 'last_name', 'password')

class AddProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfiles
        fields =['profile_pics',]