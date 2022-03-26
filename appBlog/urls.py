
from unicodedata import name
from django.urls import path
from appBlog import views

urlpatterns = [
   path('',views.BlogList.as_view(),name='blog'),
   path("page_details/<str:slug>",views.blogs_details,name='blog_details'),
   path("my-blog/page_details/<str:slug>",views.blogs_details,name='blog_details'),
   path('AddBlog/',views.CreateBlogs.as_view(),name='create_blog'),
   path('liked/<pk>/',views.blog_likes, name="blog_liked"),
   path('unliked/<pk>/',views.blog_unlikes, name="blog_unliked"),
   path('my-blog/',views.MyBlog.as_view(), name="my_blog"),
   path('edit-blog/<pk>/',views.UpdateBlog.as_view(), name="edit_blog"),
]


