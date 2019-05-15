#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="example_index"),
]
