from django.shortcuts import render

def index(request):
	return render(request,'guest/home.html')

def about(request):
	return render(request,'guest/about.html')

def contact(request):
	return render(request,'guest/contact.html')

def login(request):
	return render(request,'guest/login.html')
