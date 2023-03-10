from django.contrib import admin
from .models import Netlify

# Register your models here
@admin.register(Netlify)
class netlifyAdmin(admin.ModelAdmin):
    list_display = ["genetic", "length", "mass", "exercise", "smoking", "alcohol", "sugar", "lifespan"]
