from django.http import HttpResponse
from django.utils import timezone

from .models import Flux

def index(request):
	now = timezone.now()
	flux = Flux(date_time=now, flux=1.0)
	flux.save()
	return HttpResponse("Este mi microservicio")
