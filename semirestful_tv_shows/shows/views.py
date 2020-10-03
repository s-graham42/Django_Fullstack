from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        "all_shows": Show.objects.all(),
    }
    return render(request, 'shows.html', context)

def new(request):
    return render(request, 'new_show.html')

def create(request):
    if request.method == "POST":
        print(request.POST)
        print(request.POST['release_date'])
        new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
    return redirect('/shows/' + str(new_show.id))

def one_show(request, show_id):
    context = {
        "one_show": Show.objects.get(id=show_id)
    }
    return render(request, 'one_show.html', context)

def edit(request, show_id):
    context = {
        "one_show": Show.objects.get(id=show_id)
    }
    return render(request, 'edit_show.html', context)

def update(request, show_id):
    if request.method == "POST":
        show_to_update = Show.objects.get(id=show_id)
        show_to_update.title = request.POST['title']
        show_to_update.network = request.POST['network']
        show_to_update.release_date = request.POST['release_date']
        show_to_update.description = request.POST['description']
        show_to_update.save()
    return redirect('/shows/' + str(show_id))

def destroy(request, show_id):
    if request.method == "POST":
        show_to_delete = Show.objects.get(id=show_id)
        show_to_delete.delete()
    return redirect('/')