from django.shortcuts import render,redirect
from .models import *


def form_page(request):
    return render(request,'index.html')

def register(request):
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
