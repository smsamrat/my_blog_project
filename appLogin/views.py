import re
from django.shortcuts import redirect, render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse  
from django.contrib.auth.forms import PasswordChangeForm  

from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from appLogin.forms import signUpForm
from appLogin.forms import userchangedProfileForm, AddProfilePic


# Create your views here.
def signUp(request):
    form = signUpForm() 
    registered=False
    if request.method == 'POST':  
        form = signUpForm(data = request.POST)  
        if form.is_valid():  
            form.save()
            registered=True    
    context = {  
        'form':form,
        'registered':registered
    }  
    return render(request, 'app_login/signup.html', context)

def login_user(request):
    form =AuthenticationForm()
    if request.method == "POST":
        form =AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
            return HttpResponseRedirect(reverse('index')) 
    return render(request,'app_login/login.html',context={'form':form})

@login_required

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required
def user_profile(request):
    return render(request,'app_login/user_profile.html',context={})

@login_required
def userchangedProfile(request):
    current_user = request.user
    form = userchangedProfileForm(instance=current_user)
    if request.method =='POST':
        form = userchangedProfileForm(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            form = userchangedProfileForm(instance=current_user)
    return render(request,'app_login/userchangedProfile.html',context={'form':form})

@login_required
def changedPassword(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user,data = request.POST)
        if form.is_valid():
            form.save()
    return render(request,'app_login/changePass.html',context={'form':form})

@login_required
def Add_Profile_Pic(request):
    form = AddProfilePic()
    if request.method=='POST':
        form = AddProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_object = form.save(commit=False)
            user_object.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('user_profile'))
    return render(request,'app_login/Add_Profile_Pic.html',context={'form':form})

@login_required
def Change_Profile_Pic(request):
    form = AddProfilePic(instance=request.user.user_profiles)
    if request.method=='POST':
        form = AddProfilePic(request.POST, request.FILES,instance=request.user.user_profiles)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user_profile'))
    return render(request,'app_login/Add_Profile_Pic.html',context={'form':form})


