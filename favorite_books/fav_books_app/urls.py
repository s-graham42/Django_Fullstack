from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('create', views.create),
    path('<int:book_id>', views.show),
    path('<int:book_id>/like', views.like),
]