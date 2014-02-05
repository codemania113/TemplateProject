import json
import django


from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def load(request, addr):
    with open('json1.json', 'r') as json1_file:
        json1_data = json.load(json1_file)
        node = json1_data
        flag = 0
        lis_ele = 0
        lis = request.path.strip('/').split("/")
        for tag in lis:
            if flag == 0:
                flag = 1
                if node['slug'] == lis[-1]:
                    break
            else:
                    if node['slug'] == lis[lis_ele] and node['kind'] == 'Topic':
                        temp = lis_ele + 1
                        for child in node['children']:
                            if child['slug'] == lis[temp]:
                                node = child
                                lis_ele = lis_ele + 1
                                break
                            else:
                                continue
        if node['slug'] == lis[-1]:
            address = settings.MEDIA_URL + node['slug'] + '.jpg'
            if node['kind'] == 'Topic':
                return render(request, 'project.html', {'title': node['title'], 'node': node})
            else:
                return render(request, 'project1.html', {'title': node['title'], 'node': node , 'address':address})
        
