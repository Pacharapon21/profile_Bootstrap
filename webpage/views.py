from django.shortcuts import render

def index(request):
    return render(request, 'webpage/index.html')

def about(request):
    return render(request, 'webpage/about.html')

def home(request):
    return render(request, 'webpage/home.html')

def contact(request):
    return render(request, 'webpage/contact.html')
