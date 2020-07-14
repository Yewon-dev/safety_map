from django.shortcuts import render
import folium
import urllib.request
import datetime
import time
import json
import webbrowser
import pymysql

# Create your views here.
def home(request):
    return render(request, 'home.html')

def startpage(request):
    return render(request, 'startpage.html')

def showMaps(request):
    map = folium.Map(location=[37.6511988,127.0161604],zoom_start=12)
    maps=map._repr_html_() 
    return render(request, 'home.html',{'map':maps})

#한정원 : 안심장소보기 미완성
from safety_map.models import SafetyZone

def showSafetyZone(request):
    map = folium.Map(location=[37.6511988,127.0161604],zoom_start=12)
    maps = map._repr_html_()
    return render(request,'safetyzone.html',{'map':maps})

def showszMarker(request):
    map = folium.Map(location=[37.6511988,127.0161604],zoom_start=12)
    folium.Marker([37.566345, 126.977893],popup='testtest').add_to(map)
    i = 1 
    p = SafetyZone.objects.get(safety_zone_pk=i)
    for i in range(100):
        folium.Marker([37.566345, 126.977893],popup='testtest').add_to(map)
        i = i+1

    maps = map._repr_html_()
    return render(request,'safetyzone.html',{'map':maps})