from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from datetime import datetime
from itertools import groupby
from .forms import SearchForm
import json
import random


class MainIndex(View):
    def get(self, request, *args, **kwargs):
        return redirect('/news/')


class NewsCreate(View):
    with open(settings.NEWS_JSON_PATH, 'r') as file:
        news = json.load(file)

    def get(self, request, *args, **kwargs):
        return render(request, 'news/news_create.html',)

    def post(self, request, *args, **kwargs):
        random.seed()
        title = request.POST.get('title')
        text = request.POST.get('text')
        create = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        link = random.randint(4,999999)
        flag = True
        while flag:
            link_list = []
            for item in self.news:
                link_list.append(item['link'])
            if link in link_list:
                random.seed()
                link = random.randint(4, 999999)
            else:
                flag = False
        story = {'created': create, 'text': text, 'title': title, 'link': link}
        self.news.append(story)
        with open(settings.NEWS_JSON_PATH, 'w') as file:
            json.dump(self.news, file)
        return redirect('/news/')


def news_main(request):
    with open(settings.NEWS_JSON_PATH, 'r') as file:
        news = json.load(file)
    sorted_news = sorted(news, key=lambda x: x['created'], reverse=True)
    query = SearchForm()
    search = request.GET
    if search:
        results = []
        for item in sorted_news:
            if search['q'].lower() in item['title'].lower():
                results.append(item)
        if results:
            results_dict = {}
            for date, content in groupby(results, key=lambda x: x['created'].split()[0]):
                results_dict[date] = list(content)
            return render(request, 'news/news_search.html', {'news': results_dict})
        return render(request, 'news/search_error.html')
    news_dict = {}
    for date, content in groupby(sorted_news, key=lambda x: x['created'].split()[0]):
        news_dict[date] = list(content)
    return render(request, 'news/news_list.html', {'news': news_dict, 'form': query})


def news_detail(request, link):
    with open(settings.NEWS_JSON_PATH, 'r') as file:
        news = json.load(file)
    for item in news:
        if item['link'] == link:
            article = item
            return render(request, 'news/news_detail.html', context=article)
    return HttpResponse('<h1>Link ID not found</h1>')
