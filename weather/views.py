from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests

# Create your views here.

info = []

def index(request):

    if request.method == 'GET':
        return render(request, "index.html", {"info": info})
 
    if request.method == 'POST':

        city = request.POST["cityName"]
        url = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=b208a89751a9e7c6269d1f4600f89591&units=metric"
        response = requests.get(url)
        weather_data = response.json()

        icon = weather_data['weather'][0]['icon'];
        image_url = "https://openweathermap.org/img/wn/" + icon + "@2x.png"

        city_data = {

            "name": weather_data['name'],
            "symbol": weather_data['sys']['country'],
            "temp": weather_data['main']['temp'],
            "image": image_url,
            "description": weather_data['weather'][0]['description']
        }

        info.append(city_data)
        return HttpResponseRedirect(reverse("index"))


