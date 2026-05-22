from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "titulo": "Bienvenido a Sietch",
    }
    return render(request, "core/home.html", context)