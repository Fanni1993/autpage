from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404





from .models import Cards
def index(request):
	cardlist= Cards.objects.all()
	context= {
		'cardlist': cardlist
	}
	return render(request,'cards/index.html',context)
def welcome(request):
	text= "Welcome"
	subtext='If you are here to get more information about Autism Spectrum Disorder, go on!'
	context={
		'text': text,
		'subtext': subtext,
	}
	return render(request,'cards/welcome.html',context)
