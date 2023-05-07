# from django.shortcuts import render
#
# # Create your views here.
#
# from django.http import JsonResponse
# from django.shortcuts import render
# from templates import *
# import backend
#
# def display_weather(request):
#     city = request.POST.get('city')
#
#     if city:
#         temp, desc, wind = backend.weather_data(city)
#         return render(request, 'weather.html', {'temp': round(temp, 2), 'desc': desc, 'winds': wind})
#     else:
#         return render(request, 'index.html')
#
#
#

from django.shortcuts import render
from app.backend import weather_data

# def index(request):
#     return render(request, 'index.html')


def weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        temperature, description, wind = weather_data(city)
        context = {
            'city': city,
            'temperature': round(temperature, 2),
            'description': description,
            'wind_speed': wind[0],
            'wind_direction': wind[1]
        }
        return render(request, 'weather.html', context)
    else:
        return render(request, 'index.html')

