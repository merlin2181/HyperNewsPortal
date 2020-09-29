from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class MainIndexView(View):
    def get(self, response, *args, **kwargs):
        html = '''
<title>HyperNews Page</title>
<h1>Coming soon</h1>
'''
        return HttpResponse(html)