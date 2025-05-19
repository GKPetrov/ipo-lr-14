from django.urls import path
from .views import main_page, about_shop, about_author,spec_find,spec_info,spec_id_info

urlpatterns = [
    path('', main_page, name='main_page'),
    path('about_shop',about_shop, name='about_shop'),
    path('about_author',about_author, name='about_author'),
    path('spec',spec_find, name='spec'),
    path('spec/<int:id>/', spec_id_info, name="speciality_id_info"),
    path('spec_info',spec_info, name='spec_info')
]