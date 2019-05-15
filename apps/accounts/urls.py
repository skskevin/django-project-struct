#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.urls import path
from . import views

urlpatterns = [
    path('user_login/', views.user_login, name="user_login"),
    path('login_save/', views.login_save, name="login_save"),
    path('user_logout/', views.user_logout, name="user_logout"),
]
