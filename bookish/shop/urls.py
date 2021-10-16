"""bookish URL Configuration

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

from shop import views

urlpatterns = [
   path("" ,views.index,name='home'),
   path("books",views.books,name="books"),
   path("about",views.about,name="about us"),
   path("login",views.userlogin,name="login"),
   path("logout/",views.userlogout,name="logout"),
   path("signup",views.signup,name="signup"),
   path("sell",views.sell,name="sell"),
   path("home/" ,views.index,name='home'),
   path("cart/",views.cart,name="cart"),
   path("checkout/" ,views.checkout,name='checkout'),
   path("process_order/" ,views.processOrder,name='processOrder'),
   path("update_item" ,views.updateItem,name='update_item'),
   path("<int:id>/",views.detail,name='detail')
]
