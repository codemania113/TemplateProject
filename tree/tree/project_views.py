import json


import django
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

def load(request, addr):
    with open('json1.json', 'r') as json1_file:
        node = json.load(json1_file)
        flag = 0
        lis_element = 0
        lis = request.path.strip('/').split("/")
        for counter in lis:   # condition to enter the root node, which is in dictionary format
            if flag == 0:
                flag = 1
                previous = counter
                if node['slug'] == lis[-1]:
                    break
            else:
                    if node['slug'] == previous and node['kind'] == 'Topic':
                        for child in node['children']:
                            if child['slug'] == counter:
                                node = child
                                break
                    previous = counter            
        if node['slug'] == lis[-1]:   # the last slug of the list is checked here
            
             if node['kind'] == 'Topic':
                return render(request, 'Parent_node.html', {'node': node })
             else:
                return render(request, 'Leaf_node.html', {'node': node})
        else:
            return HttpResponse("Invalid Url")
