from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
def validate_positive(value):
    if value>0:
        return value
    else:
        raise ValidationError("Поле должно быть положительным")
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Название")
    desc = models.CharField(max_length=1000, blank=True, verbose_name = "Описание") 
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
class Producer(models.Model):
    name = models.CharField(max_length=100, verbose_name ="Название")
    country = models.CharField(max_length=100, verbose_name ="Страна")
    desc = models.CharField(max_length=1000, blank=True, verbose_name ="Описание")
    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name ="Название")
    desc = models.CharField(max_length=1000, blank=True, verbose_name ="Описание")
    product_photo = models. ImageField( verbose_name ="Фото")
    price = models.DecimalField(max_digits=10, decimal_places=2,validators =[validate_positive], verbose_name ="Цена")
    available_on_stock = models.IntegerField(validators =[validate_positive], verbose_name ="Доступно на складе")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name ="Категория")
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name ="Производитель")
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
    def __str__(self):
        return self.name
def validate_stock(value):
    if value<product.available_on_stock:
        return value
    else:
        raise ValidationError("Поле должно быть положительным")
class NewUser(AbstractUser):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
class Cart(models.Model):
    user = models.OneToOneField(NewUser,on_delete=models.CASCADE, verbose_name ="Пользователь")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name ="Дата создания")
    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
    def total_cost(self):
        total_cost=0
        for item in CartElem:
            if item.cart==self:
                total_cost+=item.elem_cost()
        return total_cost
    def __str__(self):
        return f"Корзина пользователя {user}"
class CartElem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name ="Корзина")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name ="Продукт")
    quantity = models.PositiveIntegerField(validators=[validate_stock], verbose_name ="Количество")
    class Meta:
        verbose_name = "Элемент корзины"
        verbose_name_plural = "Элементы корзины"
    def __str__(self):
        return f"{self.product} количество {self.quantity} шт."
    def elem_cost(self):
        return self.product.price * self.quantity

