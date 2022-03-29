from django.contrib import admin

#from webshop_api import models
from .models import CartItem, UserProfile

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(CartItem)