from django.shortcuts import render

def index(request):

    return render(request,'index.html')

def upload(request):

    return render(request,'upload.html')

def filter(request):

    return render(request,'filter.html')