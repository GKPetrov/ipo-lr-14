import json
id=2
info=''
with open('dump.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for item in data:
        if item['pk'] == int(id) and item['model']=='data.specialty':
            info= f"{item['fields']['code']}>> cпециальность {item['fields']['title']}, {item['fields']['c_type']}"
print(info)