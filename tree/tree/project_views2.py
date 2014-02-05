import django
import json


from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


def generate_node(request, node, addr, html):
     
    title = node['title']
    if node['slug'] == addr:
        if node['kind'] == 'Topic':
         html = render(request, 'project.html', {'title': title, 'node': node})
        else:
         address = settings.MEDIA_URL + node['slug'] + '.jpg'
         html = render(request, 'project1.html', {'title': title, 'node': node, 'address':address})
        return html
    else:
        if node['kind'] == 'Topic':
            for child in node['children']:
                html = generate_node(request, child, addr, html)
    	return html






 # Load method converts json to python dict
def load(request, addr):
    html = " "
    with open('json1.json', 'r') as json1_file:
         json1_data = json.load(json1_file)
         html = generate_node(request, json1_data, addr, html)
         return HttpResponse(html)
