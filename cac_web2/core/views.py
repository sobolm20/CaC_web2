from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def list(request):
    return render(request, "core/list.html")

def contact(request):
    return render(request, "core/contact.html")

def details(request):
    return render(request, "core/details.html")
