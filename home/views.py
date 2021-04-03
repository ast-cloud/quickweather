from django.shortcuts import render, redirect, HttpResponse
import requests
from home.models import City
from datetime import datetime


# Create your views here.

def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=e09dd0b214c71258c57a8720e48712e8'
    if request.method=='POST':
        a=requests.get(url.format(request.POST.get('newcity')))
        if a['cod']=="200":
            City(name=request.POST.get('newcity'), dt=datetime.today()).save()
            
    queryset=City.objects.all()
    allcitydata=[]
    for city in queryset:
        res=requests.get(url.format(city)).json()
        cityweather={
        'id':city.id,
        'city':city.name,
        'temp':res['main']['temp'],
        'desc':res['weather'][0]['description'],
        'icon':res['weather'][0]['icon']
        }
        allcitydata.append(cityweather)

    allcitydata.reverse()
    context={'cw':allcitydata, 'l':len(allcitydata)}
    return render(request, 'index.html', context)


def delcity(request, cid):
    City.objects.filter(id=cid).delete()
    return redirect('/')