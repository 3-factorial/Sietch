from django.db import models

# Create your models here.
class Flux(models.Model):
	date_time = models.DateTimeField("Date Time")
	flux = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
