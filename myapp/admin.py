from django.contrib import admin
from .models import Category, Product,Producer,NewUser,Cart,CartElem
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Producer)
admin.site.register(NewUser)
admin.site.register(CartElem)
admin.site.register(Cart)

