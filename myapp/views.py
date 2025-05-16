from django.shortcuts import render
import json
def main_page(request):
    return render(request, 'main.html')
def about_shop(request):
    return render(request, 'shop.html')
def about_author(request):
    return render(request, 'author.html')
def spec(request):
    return render(request, 'spec.html')
def spec_find(request):
    spec_list=[]
    with open('dump.json', 'r', encoding='utf-8') as f:     
        data = json.load(f)
        for item in data:
            if item['model']=='data.specialty':
                spec_list.append(item['fields']['title']) 
    return render(request, 'spec.html', {'spec_list':spec_list})
def spec_info(request):
    with open('dump.json', 'r', encoding='utf-8') as f:   
        for item in data:
        if item['pk'] == id and item['model']=='data.specialty':
            return f"{item['fields']['code']}>> cпециальность {item['fields']['title']}, {item['fields']['c_type']}"
        