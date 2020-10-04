from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('courses/destroy/<int:id>', views.destroy),
    path('courses/destroy/<int:id>/delete', views.delete),
]