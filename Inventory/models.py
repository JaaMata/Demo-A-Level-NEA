from django.db import models
from django.db.models.deletion import SET_NULL
from accounts.models import User, ShippingAddressModel

from random import choice
from string import ascii_lowercase


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    barcode = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10,
                                           decimal_places=2,
                                           null=True,
                                           blank=True)
    borrowed = models.BooleanField(default=False)
    coverImage = models.ImageField(upload_to='bookCovers')
    tags = models.ManyToManyField(Tag)
    payment_id = models.CharField(max_length=200, null=True)
    product_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True, null=True)
    payment_complete = models.BooleanField(default=False, null=True)
    complete = models.BooleanField(default=False, null=True)
    transaction_id = models.CharField(max_length=200, unique=True)
    shipping_address = models.ForeignKey(ShippingAddressModel,
                                         on_delete=SET_NULL,
                                         null=True)

    def __str__(self) -> str:
        return str(self.id)

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        if str(total)[-2] == '.':
            total = str(total) + '0'
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total

    def transaction_id_gen():
        string = ""
        lst = list(ascii_lowercase)
        for i in range(13):
            string = string + str(choice(lst))

        return string


class OrderItem(models.Model):
    product = models.ForeignKey(Book, on_delete=SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        if str(total)[-2] == '.':
            total = str(total) + '0'
        return total
