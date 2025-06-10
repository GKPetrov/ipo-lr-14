from django.shortcuts import render
import json
from django.http import JsonResponse
def main_page(request):
    return render(request, 'main.html')
def about_shop(request):
    return render(request, 'shop.html')
def about_author(request):
    return render(request, 'author.html')
def spec(request):
    return render(request, 'spec.html')

