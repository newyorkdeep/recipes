from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Entrie
from django.urls import reverse
from django.template import loader
# Create your views here.
def home(request):
    myentries=Entrie.objects.all().values()
    template=loader.get_template('home.html')
    context={
        'myentries':myentries,
    }
    return HttpResponse(template.render(context, request))

def addrecord(request):
    x=request.POST['title']
    q=request.POST['compound']
    c=request.POST['cooking']
    if(len(x)>2 and len(q)>2 and len(c)>2):
        entrie=Entrie(title=x, compound=q, cooking=c)
        entrie.save()
    return HttpResponseRedirect(reverse('home'))

def deleterecord(request, id):
    myentrie=Entrie.objects.get(id=id)
    myentrie.delete()
    return HttpResponseRedirect(reverse('home'))

def editrecord(request, id):
    myentrie=Entrie.objects.get(id=id)
    template=loader.get_template('editing.html')
    context={
        'myentrie': myentrie,
    }
    return HttpResponse(template.render(context,request))

def completeedit(request, id):
    myentrie=Entrie.objects.get(id=id)
    myentrie.delete()
    x=request.POST['title']
    q=request.POST['compound']
    c=request.POST['cooking']
    if(len(x)>2 and len(q)>2 and len(c)>2):
        entrie=Entrie(title=x, compound=q, cooking=c)
        entrie.save()
    return HttpResponseRedirect(reverse('home'))

def details(request, id):
    myentrie=Entrie.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'myentrie': myentrie,
    }
    return HttpResponse(template.render(context, request))

