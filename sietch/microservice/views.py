from django.http import HttpResponse
from datetime import datetime
from .models import Flux,MyUser
from django.shortcuts import render
from django.views.generic import View
from .forms import MyUserForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#chanse me equivoque


def index(request):
	data = Flux.objects.values()
	now = datetime.now()
	flux = Flux(date_time = now,flux = 1.0,name = "hello")
	flux.save()
	data = list(Flux.objects.values())
	import json
	data = json.dumps(data, default = str)
	return HttpResponse(data,content_type="application/json")


class MyUserView(View):
	form_class = MyUserForm
	template_name = 'microservice/info.html'
	initial = {"key":"value"}


	def get(self,request,*args,**kwargs):
		id_key = self.kwargs["id_key"]

		try:
			data  = MyUser.objects.get(id=id_key)
			form = self.form_class(instance=data)
		except MyUser.DoesNotExist:
			form = self.form_class(initial=self.initial)
			id_key = 0
		return render(request,self.template_name,{'form':form,'id_key':id_key})

	def post(self, request, *args, **kwargs):
		id_key = self.kwargs['id_key']

		try:
			instance = MyUser.objects.get(id=id_key)
			form = self.form_class(request.POST, instance = instance)

		except MyUser.DoesNotExist:
			form = self.form_class(request.POST)

		if form.is_valid():
			myuser = form.save(commit = False)
			if not myuser.id:
				myuser.id = id_key
			myuser.save()	
			return HttpResponse(f"Usuario {myuser.name} guardado con éxito con ID {id_key}")
				
		return render(request, self.template_name, {'form': form, 'id_key': id_key})


	#@method_decorator(login_required)
	def dispatch(self,*args,**kwargs):
		return super(MyUserView,self).dispatch(*args,**kwargs)
	#return HttpResponse(data,content_type="application/json")

