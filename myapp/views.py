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
def spec_find(request):
    spec_list=[]
    with open('dump.json', 'r', encoding='utf-8') as f:     
        data = json.load(f)
        for item in data:
            if item['model']=='data.specialty':
                spec_data={
                    'title':item['fields']['title'] ,
                    'pk':item['pk']
                    }
                spec_list.append(spec_data)
    return render(request, 'spec.html', {'spec_list':spec_list })
def spec_info(request):
    id = request.GET.get('id')
    info=''
    with open('dump.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            if item['pk'] == int(id) and item['model']=='data.specialty':
                info= f"{item['fields']['code']}>> cпециальность {item['fields']['title']}, {item['fields']['c_type']}"
    return render(request, 'spec_info.html' ,{'info' :info})
def spec_id_info(request, id):
    info=''
    with open('dump.json', 'r', encoding='utf-8') as f:
        data = json.load(f)  
        for item in data:
            if item['pk'] == int(id) and item['model']=='data.specialty':
                info= f"{item['fields']['code']}>> cпециальность {item['fields']['title']}, {item['fields']['c_type']}"
    return render(request, 'spec_info.html' ,{'info' :info})