from django.shortcuts import render

# Create your views here.

from app.models import *

def display_topics(request):

    LTO=Topic.objects.all()
    d={'LTO':LTO}

    return render(request,'display_topics.html',d)

def display_web(request):

    LWO=Webpage.objects.filter(topic_name='SRH').update(email='Makram@gmail.com')
    LWO=Webpage.objects.filter(topic_name='RCB').update(email='Virat@gmail.com')
    LWO=Webpage.objects.filter(name='Makram').update(topic_name='SRH')
    TO=Topic.objects.get_or_create(topic_name='GT')[0]
    TO.save()
    LWO=Webpage.objects.update_or_create(name='Pandya', defaults={'email':'pandya@gmail.com','topic_name':TO})
    
    
    
    

    LWO=Webpage.objects.all()
    d={'LWO':LWO}

    return render(request,'display_web.html',d)

def display_access(request):

    LAO=Access.objects.filter(name='Makram').delete()
    LAO=Access.objects.filter(author='Hitman').delete()
    LAO=Access.objects.all().delete()

    LAO=Access.objects.all()
    d={'LAO':LAO}

    return render(request,'display_access.html',d)