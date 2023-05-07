# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.display_weather, name='display_weather'),
#     path('', views.weather, name='weather'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather, name='index'),
    path('weather/', views.weather, name='weather'),
]

