

from django.urls import path
from . import views

urlpatterns = [
   path('signup/',views.signUp, name='signup'),
   path('login/',views.login_user, name='login'),
   path('logout/',views.logout_user, name='logout'),
   path('user_profile/',views.user_profile, name='user_profile'),
   path('userchangedProfile/',views.userchangedProfile, name='userchangedProfile'),
   path('changePass/',views.changedPassword, name='changePass'),
   path('Add-Profile-Pic/',views.Add_Profile_Pic, name='Add_Profile_Pic'),
]
