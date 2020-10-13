from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_pw)
            request.session['current_user'] = new_user.id
            return redirect('/books')
    return redirect('/')

def login(request):
    if request.method =="POST":
        login_user = User.objects.filter(email=request.POST['email'])
        if len(login_user) > 0:
            login_user = login_user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), login_user.password.encode()):
                request.session["current_user"] = login_user.id
                return redirect('/books')
        messages.error(request, "Email or password is incorrect.")
        return redirect('/')
    return redirect('/')

def success(request):
    if 'current_user' not in request.session:
        messages.error(request, "Please register or log in.")
        return redirect('/')
    else:
        context = {
            "curr_user": User.objects.get(id=request.session['current_user'])
        }
        return render(request, 'success.html', context)

def log_out(request):
    request.session.clear()
    return redirect('/')
