
from django.urls import path
from appBlog import views

urlpatterns = [
   path('',views.BlogList.as_view(),name='blog'),
   path('AddBlog/',views.CreateBlogs.as_view(),name='create_blog')
]


