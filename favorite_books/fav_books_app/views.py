from django.shortcuts import render, redirect
from django.contrib import messages
from login.models import User
from .models import Book

# Create your views here.
def books(request):
    if 'current_user' not in request.session:
        messages.error(request, "Please register or log in.")
        return redirect('/')
    context = {
        'curr_user': User.objects.get(id=request.session['current_user']),
        'all_books': Book.objects.all(),
    }
    return render(request, 'books.html', context)

def create(request):
    if 'current_user' not in request.session:
        messages.error(request, "Please register or log in.")
        return redirect('/')
    if request.method =="POST":
        errors = Book.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/books')
        else:
            curr_user = User.objects.get(id=request.session['current_user'])
            new_book = Book.objects.create(title=request.POST['title'], desc=request.POST['description'], uploaded_by=curr_user)
            new_book.liked_by.add(curr_user)
            return redirect('/books')
    return redirect('/books')

def show(request, book_id):
    if 'current_user' not in request.session:
        messages.error(request, "Please register or log in.")
        return redirect('/')
    this_book = Book.objects.filter(id=book_id)
    if len(this_book) == 0:
        messages.error(request, "Book id doesn't exist.")
        return redirect('/books')
    else:
        this_book = this_book[0]
        context = {
            'curr_user': User.objects.get(id=request.session['current_user']),
            'this_book': this_book,
            'favorited': User.objects.filter(books_liked=this_book)
        }
        #if it's owned by the current user, show an edit page.
        if this_book.uploaded_by.id == request.session['current_user']:
            return render(request, 'edit.html', context)
        # if it's not, show an informational Page.
        else:
            return render(request, 'show.html', context)
    return redirect('/books')

def like(request, book_id):
    if 'current_user' not in request.session:
        messages.error(request, "Please register or log in.")
        return redirect('/')
    this_book = Book.objects.filter(id=book_id)
    if len(this_book) == 0:
        messages.error(request, "Book id doesn't exist.")
        return redirect('/books')
    this_book = this_book[0]
    curr_user = User.objects.get(id=request.session['current_user'])
    this_book.liked_by.add(curr_user)
    return redirect (f'/books/{book_id}')