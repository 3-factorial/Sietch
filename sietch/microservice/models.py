from django.db import models

# Create your models here.
class Flux(models.Model):
	date_time = models.DateTimeField("Date Time")
	flux =  models.DecimalField(default = 0.0)
