from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import MainIndex, NewsCreate

app_name = 'news'
urlpatterns = [
    path('', MainIndex.as_view(), name='index'),
    path('news/', views.news_main, name='main_index'),
    path('news/<int:link>/', views.news_detail, name='news_detail'),
    path('news/create/', NewsCreate.as_view(), name='create'),
]

urlpatterns += static(settings.STATIC_URL)