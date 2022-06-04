from telnetlib import LOGOUT
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
def home(request):
    
    return render(request, "base.html")


def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,"users/login.html",{
                "error" :"Kullanıcı Bulunamadı."
            })
    return render(request,"users/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request,"users/register.html",{"error" : "Bu kullanıcı adı bulunmaktadır"})
            elif User.objects.filter(email=email).exists():
                return render(request,"users/register.html",{"error" : "Bu email adı bulunmaktadır"})
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect("/")
        else:
            return render(request,"users/register.html",{"error" : "Password adı bulunmaktadır"})
    return render(request,"users/register.html")
            
    

def logout_request(request):
    logout(request)
    return redirect("/")