#!/usr/bin/env python

from rest_framework import serializers
from .models import Netlify

class NetlifySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Netlify
        fields = ["genetic", "length", "mass", "exercise", "smoking", "alcohol", "sugar", "lifespan"]