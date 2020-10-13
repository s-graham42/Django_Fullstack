from django.shortcuts import render, HttpResponse, redirect
from login.models import User
from .models import Author, Book, Review
from django.contrib import messages


# Create your views here.
def main_page(request):
    if 'current_user' not in request.session:
        messages.error(request, "Please register or log in.")
        return redirect('/')
    context = {
        "curr_user": User.objects.get(id=request.session['current_user']),
    }
    return render(request, 'main_page.html', context)

def add(request):
    if 'current_user' not in request.session:
        messages.error(request, "Please register or log in.")
        return redirect('/')
    context = {
        "curr_user": User.objects.get(id=request.session['current_user']),
    }
    return render(request, 'add.html', context)

def create(request):
    # check for login
    if 'current_user' not in request.session:
        messages.error(request, "Please register or log in.")
        return redirect('/')
    # validate book
    if request.method == "POST":
        book_errors = Book.objects.book_validator(request.POST)
        author_errors = Author.objects.author_validator(request.POST)
        review_errors = Review.objects.review_validator(request.POST)
        errors = book_errors
        errors.update(author_errors)
        errors.update(review_errors)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/books/add')
        else:
            # create the stuff
            curr_user = User.objects.get(id=request.session['current_user'])
            new_author = Author.objects.create(name=request.POST['author'])
            new_book = Book.objects.create(title=request.POST['title'], author=new_author, added_by=curr_user)
            Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], reviewed_by=curr_user, book_reviewed=new_book)
            return redirect('/books')
    return redirect('/books')

def one_book(request, book_id):
    pass