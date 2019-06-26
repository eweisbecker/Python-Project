from django.shortcuts import render, redirect

def home(request):
	return render(request, 'project_app/home.html')

def login(request):
    return render(request, 'project_app/home.html')