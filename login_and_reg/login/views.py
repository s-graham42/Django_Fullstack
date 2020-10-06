from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        pass
    return redirect('/')

def login(request):
    if request.method =="POST":
        pass
    return redirect('/')

def success(request):

    return render(request, 'success.html')
