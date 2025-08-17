from django.shortcuts import render

def index(request):
	return render(request, 'webprofile/index.html')

def home(request):
	return render(request, 'webprofile/home.html')

def about(request):
	return render(request, 'webprofile/about.html')

def contact(request):
	return render(request, 'webprofile/contact.html')
