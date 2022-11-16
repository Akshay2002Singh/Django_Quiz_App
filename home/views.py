from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from home.models import contact


# Create your views here.
def index(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()
    return render(request,'index.html',context)

def login_user(request):
    return render(request,'login.html')

def login_form(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password= password)
        if user is not None:
            login(request,user)
            return redirect ("/")
        else:
            return redirect("/login")

def create_user(request):
    return render(request,"sign_up.html")

def create_user_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username,email,password)
        user.first_name=name
        user.save()
        return render(request,'login.html')

def log_out(request):
    logout(request)
    return redirect("/")

def contact_us(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()
    return render(request,"contact_us.html",context)

def submit_contact_form(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        temp_contact = contact(name=name,email=email,phone=phone,message=message)
        temp_contact.save()

        return render(request,'contact_us.html',context)

