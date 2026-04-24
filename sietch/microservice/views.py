from django.shortcuts import render
from django.http import HttpResponse
from .models import Flux
# Create your views here.
from django.http import HttpResponse

def index(request):
	now = datetime.now
	flux = Flux(now, 1.0)
	flux.save()
	return HttpResponse("Este mi microservicio")
