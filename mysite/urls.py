"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import render_login,render_register, signout, render_index, render_myproducts, render_buys, render_addproducts, render_updateproduct, delete_product, mark_as_selled
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',render_login, name='login'),
    path('register/',render_register, name='register'),
    path('logout/', signout, name='logout'),
    path('marketplace/', render_index, name='index'),
    path('myproducts/', render_myproducts, name='my_products'),
    path('buys/', render_buys, name='buys'),
    path('addproducts/', render_addproducts, name='add_products'),
    path('updateproduct/<int:product_id>/', render_updateproduct, name='update_product'),
    path('deleteproduct/<int:product_id>/', delete_product, name='delete_product'),
    path('mark_as_selled/<int:product_id>', mark_as_selled, name='mark_as_selled')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
