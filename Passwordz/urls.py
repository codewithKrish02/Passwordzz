"""Passwordz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from sitehandler.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexpage,name='indexpage'),
    path('createaccount/',registration,name='registration'),
    path('logout/',Logout,name='logout'),
    path('password/',addnewpassword,name='addnewpassword'),
    path('personalinfo/',addpersonalinfo,name='addpersonalinfo'),
    path('payments/',addpayments,name='addpayments'),
    path('ids/',addids,name='addids'),
    path('notes/',addsecurenotes,name='addsecurenotes'),
    path('deletename<int:pid>',delete_name,name='delete_name'),
    path('deleteemail<int:pid>',delete_email,name='delete_email'),
    path('deletephone<int:pid>',delete_phone,name='delete_phone'),
    path('deleteaddress<int:pid>',delete_address,name='delete_address'),
    path('deletecompany<int:pid>',delete_company,name='delete_company'),
    path('deleteweb<int:pid>',delete_web,name='delete_web'),
    path('deletecard<int:pid>',delete_card,name='delete_card'),
    path('deleteidcard<int:pid>',delete_idcard,name='delete_idcard'),
    path('deletedriverlicense<int:pid>',delete_driverlicense,name='delete_driverlicense'),
    path('deletepassport<int:pid>',delete_passport,name='delete_passport'),
    path('deletetax<int:pid>',delete_tax,name='delete_tax'),
    path('deletenotes<int:pid>',delete_notes,name='delete_notes'),
    path('deletepassword<int:pid>',delete_password,name='delete_password'),
    #path('decryptpass<int:pid>',decryptpass,name='decryptpass'),
]
