import datetime

from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    product_id = models.CharField(max_length=20,
                                  primary_key=True,
                                  unique=True)
    product_name = models.CharField(max_length=30)
    category_id = models.ForeignKey('Category',
                                    on_delete=models.CASCADE)
    supplier_id = models.ForeignKey('Supplier',
                                    on_delete=models.CASCADE)
    quantity_per_unit = models.IntegerField()
    unit_price = models.IntegerField()

    def __str__(self):
        return f'{self.product_id} {self.product_name}'

    objects = models.Manager()


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    category_id = models.CharField(max_length=20,
                                   primary_key=True,
                                   unique=True)
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.category_id} {self.category_name}'

    objects = models.Manager()


class Supplier(models.Model):
    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    supplier_id = models.CharField(max_length=10,
                                   primary_key=True,
                                   unique=True)
    company_name = models.CharField(max_length=30)
    contact_name = models.CharField(max_length=30)
    contact_title = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    is_verified = models.BooleanField(default=False,
                                      null=True)
    created = models.DateTimeField(auto_created=True,
                                   default=datetime.datetime.now())

    def __str__(self):
        return f'{self.supplier_id} {self.company_name}'

    objects = models.Manager()


class Employee(models.Model):
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    employee_id = models.IntegerField(primary_key=True,
                                      unique=True)
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.CharField(max_length=30,
                             unique=True)
    address = models.CharField(max_length=30)
    department = models.ForeignKey('Category',
                                   on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.employee_id} {self.name} {self.surname}'

    objects = models.Manager()


class Feedback(models.Model):
    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    positive_negative = [
        ('+', 'Positive'),
        ('-', 'Negative')
    ]
    mark = [
        ('1', '1 - Bad'),
        ('2', '2 - Better'),
        ('3', '3 - Normal'),
        ('4', '4 - Not enough'),
        ('5', '5 - Good'),

    ]

    image = models.ImageField(upload_to='images/',
                              null=True,
                              blank=True)
    user_email = models.CharField(max_length=20,
                                  unique=True)
    description = models.CharField(max_length=100,
                                   unique=True)
    mark = models.CharField(choices=mark,
                            max_length=9)
    short_mark = models.CharField(choices=positive_negative,
                                  max_length=9)
    phone_number = models.CharField(max_length=10,
                                    unique=True)
    created = models.DateTimeField(auto_created=True,
                                   default=datetime.datetime.now())
    written_by = models.ForeignKey(User, verbose_name='Written by', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_email} {self.mark}'

    objects = models.Manager()


class Game(models.Model):
    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    user = models.CharField(max_length=4,
                            default='PING')
    computer = models.CharField(max_length=4,
                                default='PONG')
