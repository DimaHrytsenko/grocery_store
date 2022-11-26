from django.contrib import admin

from grocery_store.models import Category, Supplier, Product, Employee, Feedback, Game

# Register your models here.
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(Feedback)
admin.site.register(Game)
