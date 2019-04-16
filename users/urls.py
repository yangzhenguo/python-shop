#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 2019/4/16
from __future__ import print_function
from django.conf.urls import url

import views

__author__ = 'Sam'


urlpatterns = [
    url(r'^register/', views.register, name='register'),
]