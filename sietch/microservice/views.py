from django.http import HttpResponse
from datetime import datetime
from .models import Flux
from django.shortcuts import render


def index(request):
	data = Flux.objects.values()
	now = datetime.now()
	flux = Flux(now,1.0,"hello")
	flux.save()
	return HttpResponse(data,content_type="application/json")
