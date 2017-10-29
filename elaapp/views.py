from django.shortcuts import render, render_to_response
from django.template import RequestContext
from . import models as m
from django.shortcuts import render
# Create your views here.
def index(request):
    if request.method == "POST":
        
        m.Contactus.objects.create(name=request.POST['name'], email=request.POST['email'],subject=request.POST['subject'],message=request.POST['message']) 
        #contact = m.Contactus()
        #contact.name = request.POST['name']
        #contact.email = request.POST['email']
        #contact.subject = request.POST['subject']
        #contact.message = request.POST['message']
        #contact.save   
	    

    return render(request, 'index.html')
	
	
def about(request):
    return render_to_response('about.html',{})
def analy(request):
    return render_to_response('analy.html',{})
def integration(request):
    return render_to_response('integration.html',{})
def market(request):
    return render_to_response('market.html',{})
def track(request):
    return render_to_response('track.html',{})
def careers(request):
    return render_to_response('careers.html',{})
