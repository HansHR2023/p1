#!/usr/bin/env python

from django.contrib import admin
from django.urls import path, include
from rest_api import urls as rest_urls
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('medish_centrum_randstad/', include(rest_urls)),
]

