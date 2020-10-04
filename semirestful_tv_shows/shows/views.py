from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages
from datetime import date
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
        errors = Show.objects.new_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:
            new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
            return redirect('/shows/' + str(new_show.id))
    return redirect('/shows/new')

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
        errors = Show.objects.edit_validator(request.POST, show_id)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/'+ str(show_id) + '/edit')
        else:
            show_to_update = Show.objects.get(id=show_id)
            show_to_update.title = request.POST['title']
            show_to_update.network = request.POST['network']
            show_to_update.release_date = request.POST['release_date']
            show_to_update.description = request.POST['description']
            show_to_update.save()
            return redirect('/shows/' + str(show_id))
    return redirect('/')

def destroy(request, show_id):
    if request.method == "POST":
        show_to_delete = Show.objects.get(id=show_id)
        show_to_delete.delete()
    return redirect('/')