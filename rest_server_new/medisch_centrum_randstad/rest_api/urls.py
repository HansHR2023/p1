#!/usr/bin/env python

from .views import NetlifyListApiView
from django.urls import path
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
# from django.views.generic.base import RedirectView

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico'))),
    path('api/netlify', NetlifyListApiView.as_view())
]
