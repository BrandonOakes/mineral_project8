from django.conf.urls import url
from django.urls import path
from .models import Mineral
from . import views

urlpatterns = [
    path('', views.mineral_list, name= 'list'),
    path('detail/<int:pk>', views.mineral_detail, name = 'detail'),
    path('search/', views.mineral_search, name='search'),
]
