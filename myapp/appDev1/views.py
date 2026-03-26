from django.shortcuts import render

def index(request):
    return render(request, 'appDev1/index.html')
