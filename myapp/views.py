from django.shortcuts import render

def main_page(request):
    return render(request, 'main.html')
def about_shop(request):
    return render(request, 'shop.html')
def about_author(request):
    return render(request, 'author.html')
