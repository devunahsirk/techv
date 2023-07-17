from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"auth/index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        messages.success(request, "Your account is created")

        return redirect('signin')




    return render(request,"auth/signup.html")

def signin(request):
    return render(request,"auth/signin.html")

def signout(request):
    pass    