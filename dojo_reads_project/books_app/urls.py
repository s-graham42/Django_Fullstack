from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('add', views.add),
    path('<int:book_id>', views.one_book),
    path('create', views.create),
]
