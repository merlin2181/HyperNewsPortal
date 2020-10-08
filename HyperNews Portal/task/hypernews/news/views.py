from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json


with open(settings.NEWS_JSON_PATH, 'r') as file:
    news = json.load(file)


class MainIndex(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Coming soon</h1>")


def news_detail(request, link):
    for item in news:
        if item['link'] == link:
            article = item
            return render(request, 'news/news_detail.html', context=article)
    return HttpResponse('<h1>Link ID not found</h1>')
