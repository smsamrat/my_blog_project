
from django.urls import path
from appBlog import views

urlpatterns = [
   path('',views.BlogList.as_view(),name='blog'),
   # path('course/<str:slug>',views.blogs_details,name='blog_details'),
   path("page_details/<str:slug>",views.blogs_details,name='blog_details'),
   path('AddBlog/',views.CreateBlogs.as_view(),name='create_blog')
]


