from django.contrib import admin
from .models import *

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('productName', 'productSKU', 'productPrice','productCategory',
                    'productStatus')
    fieldsets = [
        ('Category',        {'fields': ['productCategory']}),
        ('Product Details', {'fields': ['productName', 'productSKU',
                                        'productPrice', 'productDesc']}),
        ('Measurements',    {'fields': ['productSize']}),
        ('Colors',          {'fields': ['productColor']})
    ]

class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('productSize', 'waistSize', 'lowHipSize', 'thighSize')

    fieldsets = [
        ('Measurements Details', {'fields': ['productSize', 'waistSize',
                                        'lowHipSize', 'thighSize']})
    ]

class UsersAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'email', 'sex', 'userCreated', 'userStatus')

    fieldsets = [
        ('Personal Details', {'fields': ['fullName', 'email',
                                        'password', 'sex', 'userStatus']})
    ]

class ShippingAdmin(admin.ModelAdmin):
    list_display = ('shippingName', 'shippingDesc', 'shippingPrice')

    fieldsets = [
        ('Shipping Details', {'fields': ['shippingName', 'shippingDesc',
                                        'shippingPrice']})
    ]

admin.site.register(Country)
admin.site.register(Address)
admin.site.register(Discount)
admin.site.register(Shipping, ShippingAdmin)
admin.site.register(Orders)
admin.site.register(Users, UsersAdmin)
admin.site.register(Category)
admin.site.register(ProductSize, ProductSizeAdmin)
admin.site.register(ProductColor)
admin.site.register(Products, ProductsAdmin)
