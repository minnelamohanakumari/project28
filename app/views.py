from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.
from app.models import *
def display_topics(request):
    LTO=Topic.objects.all()
    LTO=Topic.objects.order_by('topic_name')
    d={'topics':LTO}
    return render(request,'display_topics.html',d)
def display_webpages(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.exclude(topic_name='cricket')
    LWO=Webpage.objects.order_by('-name')
    LWO=Webpage.objects.order_by('name')
    LWO=Webpage.objects.order_by(Length('name'))
    LWO=Webpage.objects.filter(name__gt='dhoni')
    LOW=Webpage.objects.order_by(Length('name').desc())
    d={'webpage':LWO}
    return render(request,'display_webpages.html',d)
def display_accessrecords(request):
    LOA=AccessRecords.objects.all()
    LOA=AccessRecords.objects.order_by('author')
    LOA=AccessRecords.objects.order_by('-author')
    LOA=AccessRecords.objects.exclude(author='abc')
    LOA=AccessRecords.objects.order_by(Length('date').desc())
    LOA=AccessRecords.objects.filter(date__gt='1998-09-13')
    LOA=AccessRecords.objects.filter(date__lt='1996-09-14')
    LOA=AccessRecords.objects.order_by(Length('author').desc())
    d={'access':LOA}
    return render(request,'display_accessrecords.html',d)
