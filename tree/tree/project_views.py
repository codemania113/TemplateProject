import json


import django
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

def load(request, addr):
    with open('json1.json', 'r') as json1_file:
        node = json.load(json1_file)
        lis = request.path.strip('/').split("/")
        if node['slug'] == lis[0]:
            if node['slug'] == lis[-1]:
                return render(request, 'Parent_node.html', {'node': node})
            else:
                prev_element = lis[0]
                for element in lis[1:]:
                    if node['slug'] == prev_element and node['kind'] == 'Topic':
                        for child in node['children']:
                            if child['slug'] == element:
                                node = child
                                break
                    prev_element = element


        if node['slug'] == lis[-1]:   # the last slug of the list is checked here
            
             if node['kind'] == 'Topic':
                return render(request, 'Parent_node.html', {'node': node })
             else:
                return render(request, 'Leaf_node.html', {'node': node})
        else:
            return HttpResponse("Invalid Url")


