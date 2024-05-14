from django.contrib import admin

# Register your models here.

from app.models import Product, Customer

admin.site.register(Customer)
admin.site.register(Product)