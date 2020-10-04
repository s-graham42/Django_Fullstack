from django.shortcuts import render, HttpResponse, redirect
from .models import Course, Description
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'all_courses': Course.objects.all(),
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        errors = Course.objects.course_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:    
            new_course = Course.objects.create(course_name=request.POST['course_name'])
            Description.objects.create(desc=request.POST['description'], course=new_course)
            return redirect('/')
    return redirect('/')

def destroy(request, id):
    context = {
        "one_course": Course.objects.get(id=id),
    }
    return render(request, 'destroy.html', context)

def delete(request, id):
    if request.method == "POST":
        course_to_delete = Course.objects.get(id=id)
        course_to_delete.delete()
    return redirect('/')