from django.urls import path
from .views import main_page, about_shop, about_author

urlpatterns = [
    path('', main_page, name='main_page'),
    path('about_shop',about_shop, name='about_shop'),
    path('about_author',about_author, name='about_author')
]