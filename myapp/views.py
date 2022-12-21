from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages


def form_page(request):
    return render(request,'index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0 :
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        if request.method == "POST":
            Register(request)
        return redirect('/')

def login(request):
    if request.method == "POST":
        if Login(request):
            id = request.session['userid'] 
            user = User.objects.get(id=id)
            context = {
                "user" : user
            }
            return render(request,'result.html',context)

    return redirect('/')
