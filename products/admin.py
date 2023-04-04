from django.contrib import admin
from products.models import Products, Comment

# Register your models here.

admin.site.register(Products)
admin.site.register(Comment)