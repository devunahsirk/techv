from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messsages



# Create your views here.
def home(request):    
    return render(request, "home.html")
def signup(request):

    if request.method =="POST":
        username=request.POST['username']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser = User.objetcs.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messsages.success(request,"Your account is succesfully created")
        return redirect('signin')





    return render(request, "signup.html")
def signin(request):
    return render(request, "signin.html")
def signout(request):
    pass

