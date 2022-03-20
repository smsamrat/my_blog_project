
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('appLogin.urls')),
    path('blog/',include('appBlog.urls')),
    path('',views.index,name='index'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
