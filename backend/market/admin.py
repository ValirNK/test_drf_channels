from .models import Product, Type, Client
from django.contrib import admin

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'currency', 'in_stock', 'date_update', 'manufacturer']
    class Meta:
        model = Product

class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    class Meta:
        model = Type

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'adress']
    filter_horizontal = ["cart"]
    class Meta:
        model = Client

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Client, ClientAdmin)

