import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Country(models.Model):
    countryName = models.CharField('Country Name', max_length=50, primary_key=True)

class Address(models.Model):
    addressOne = models.CharField('Address 1', max_length=200)
    addressTwo = models.CharField('Address 2', max_length=200)
    postalCode = models.IntegerField('Postal Code')

    #ForeignKey
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Users(models.Model):
    fullName = models.CharField(max_length=200)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    userCreated = models.DateTimeField('Created', default=timezone.now)
    userStatus = models.BooleanField('Status', default=True)

    #ForeignKey
    userAddress = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

class Category(models.Model):
    categoryName = models.CharField('Category Name', max_length=200, primary_key=True)

    def __str__(self):
        return self.categoryName

class ProductSize(models.Model):
    productSize = models.CharField('Size', max_length=5, primary_key=True)
    waistSize = models.CharField('Waist', max_length=5, default=None)
    lowHipSize = models.CharField('Low Hip', max_length=5, default=None)
    thighSize = models.CharField('Thigh', max_length=5, default=None)

    def __str__(self):
        return self.productSize

class ProductColor(models.Model):
    productColor = models.CharField('Color', max_length=20, primary_key=True)

    def __str__(self):
        return self.productColor

class Discount(models.Model):
    discount = models.FloatField('Discount', primary_key=True)

class Shipping(models.Model):
    shippingName = models.CharField('Shipping Name', max_length=100, primary_key=True)
    shippingDesc = models.TextField('Description')
    shippingPrice = models.FloatField('Price', default=0)

class Products(models.Model):
    productSKU = models.CharField('SKU', max_length=200, primary_key=True)
    productName = models.CharField('Product Name', max_length=200)
    productDesc = models.TextField('Description', default=None)
    productPrice = models.FloatField('Price', default=0)
    productStatus = models.BooleanField('Status', default=True)

    # ForeignKey
    productSize = models.ManyToManyField(ProductSize)
    productColor = models.ManyToManyField(ProductColor)
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE)

class Orders(models.Model):
    orderId = models.AutoField('Order ID', primary_key=True)


class ProductPicture(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    productColor = models.ForeignKey(ProductColor, on_delete=models.CASCADE)
    productImage = models.ImageField(default=None)
