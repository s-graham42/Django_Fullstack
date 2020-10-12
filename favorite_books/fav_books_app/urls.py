from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('create', views.create),
    path('<int:book_id>', views.show),
    path('<int:book_id>/like', views.like),
    path('<int:book_id>/un_like', views.un_like),
    path('<int:book_id>/update', views.update),
    path('<int:book_id>/destroy', views.destroy),
]