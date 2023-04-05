from django.shortcuts import render

# Create your views here.
from app.models import *
def display_topics(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    return render(request,'display_topics.html',d)
def display_webpages(request):
    LWO=Webpage.objects.all()
    d={'webpage':LWO}
    return render(request,'display_webpages.html',d)
