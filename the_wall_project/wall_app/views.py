from django.shortcuts import render, redirect
from django.contrib import messages
from login.models import User
from .models import Msg, Comment

# Create your views here.
def main_wall(request):
    if "current_user" not in request.session:
        messages.error(request, "Please register or log in.")
        return redirect('/')
    context = {
        "curr_user": User.objects.get(id=request.session['current_user']),
        "all_messages": Msg.objects.all().order_by('-created_at'),
        "all_comments": Comment.objects.all().order_by('created_at'),
    }
    return render(request, "main_wall.html", context)

def create_message(request):
    if "current_user" not in request.session:
        messages.error(request, "Please register or log in.")
        return redirect('/')
    if request.method == "POST":
        errors = Msg.objects.msg_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/wall')
        else:
            curr_user = User.objects.get(id=request.session['current_user'])
            Msg.objects.create(msg=request.POST['new_message'], user=curr_user)
            return redirect('/wall')
    return redirect('/wall')

def create_comment(request):
    if "current_user" not in request.session:
        messages.error(request, "Please register or log in.")
        return redirect('/')
    if request.method == "POST":
        errors = Comment.objects.comment_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/wall')
        else:
            curr_user = User.objects.get(id=request.session['current_user'])
            curr_message = Msg.objects.get(id=request.POST['msg_id'])
            Comment.objects.create(comment=request.POST['new_comment'], user=curr_user, msg=curr_message)
            return redirect('/wall')
    return redirect('/wall')

def destroy_message(request):
    if "current_user" not in request.session:
        messages.error(request, "Please register or log in.")
        return redirect('/')
    if request.method == "POST":
        msg_to_delete = Msg.objects.get(id=request.POST['msg_id'])
        if msg_to_delete.user.id == request.session['current_user']:
            msg_to_delete.delete()
            return redirect('/wall')
        else:
            messages.error(request, "Not your message to delete.")
            return redirect('/wall')
    return redirect('/wall')
