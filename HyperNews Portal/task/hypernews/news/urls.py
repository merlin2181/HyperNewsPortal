from django.urls import path
from . import views
from .views import MainIndex

app_name = 'news'
urlpatterns = [
    path('', MainIndex.as_view(), name='index'),
    path('news/', MainIndex.as_view(), name='main_index'),
    path('news/<int:link>/', views.news_detail, name='news_detail'),
]