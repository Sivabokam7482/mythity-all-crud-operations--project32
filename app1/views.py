from django.shortcuts import render
from app1.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
def display_topics(request):
    QST=Topic.objects.all()
    Topic.objects.filter(topic_name='Cricket')
    d={'topics':QST}
    return render(request,'display_topic.html',d)


def display_webpages(request):
    QSW=Webpage.objects.all()
    
    QSW=Webpage.objects.filter(url__startswith='https')
    QSW=Webpage.objects.filter(url__endswith='com')
    
    QSW=Webpage.objects.filter(name__startswith='M')
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(name__contains='d')    
    QSW=Webpage.objects.filter(name__regex='\w{3}')
    QSW=Webpage.objects.filter(name__in=['siva','MSD','RAMA'])
    QSW=Webpage.objects.filter(Q(topic_name='cricket') | Q(name='siva'))
    QSW=Webpage.objects.all()
    #QSW=Webpage.objects.filter(Q(topic_name='Volley Ball') & Q(url__startswith='http'))
    d={'webpages':QSW}
    return render(request,'display_webpage.html',d)
    
def display_access(request):
    
    QSA=AccessRecord.objects.all()
    QSA=AccessRecord.objects.filter(date='2022-07-11')    
    QSA=AccessRecord.objects.filter(date__gt='2022-07-11')    
    QSA=AccessRecord.objects.filter(date__gte='2022-07-11') 
    QSA=AccessRecord.objects.filter(date__lte='2023-07-11')
    QSA=AccessRecord.objects.all()
    QSA=AccessRecord.objects.filter(date__year='2022')  
    QSA=AccessRecord.objects.filter(date__month='5')    
    QSA=AccessRecord.objects.filter(date__day='17')   
    QSA=AccessRecord.objects.filter(date__year__gt='2022')
    d={'access':QSA}
    return render(request,'display_Access.html',d)

def update_webpage(request):
    #Webpage.objects.filter(name='virat').update(url='https://Virat.in')
    #Webpage.objects.filter(topic_name='cricket').update(name='MSD')
    #Webpage.objects.filter(name='virat').update(topic_name='cricket')
    #Webpage.objects.filter(url='https://Virat.in').update(name='virat')
    #Webpage.objects.filter(name='pawan').update(topic_name='Hockey')
    Webpage.objects.update_or_create(name='MSD',defaults={'url':'https://MSD.in'})
    T=Topic.objects.get_or_create(topic_name='cricket')[0]
    T.save()
    Webpage.objects.update_or_create(name='ashu',defaults={'topic_name':T,'url':'https://suresh.in'})

    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpage.html',d)


def delete_webpage(request):
    Webpage.objects.filter(name='ashu').delete()
    #Webpage.objects.filter(topic_name='cricket').delete()
    #Webpage.objects.filter(name='Rama').delete()
    #Webpage.objects.all().delete()
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpage.html',d)


