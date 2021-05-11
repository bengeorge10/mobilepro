"""mobileproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .views import index, list_mobiles, add_product, mobile_detail, update, mobile_delete, login_user, registration, \
    signout,index_admin,order,view_my_orders,cancel_order,admin_mobile_list,admin_mobile_details,view_cart,add_to_cart,\
    remove_cart_item


urlpatterns = [
    path('', index, name="index"),
    path('mobiles/', list_mobiles, name="listmobiles"),
    path('adminlist',admin_mobile_list,name='adminlist'),
    path('addproduct', add_product, name="addproduct"),
    path('mobiles/<int:id>', mobile_detail, name="detail"),
    path('adminmobiles/<int:id>',admin_mobile_details,name="adminview"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', mobile_delete, name="delete"),
    path('registration/', registration, name="register"),
    path('login/', login_user, name="userlogin"),
    path('logout/', signout, name="logout"),
    path('adminhome', index_admin, name="adminhome"),
    path('mobile/order/<int:id>', order, name="order"),
    path('vieworder/', view_my_orders, name="vieworder"),
    path('cancelorder/<int:id>', cancel_order, name="cancelorder"),
    path('addtocart/<int:id>',add_to_cart,name="addtocart"),
    path('viewcart/',view_cart,name="viewcart"),
    path('remove/<int:id>',remove_cart_item,name="remove"),
]