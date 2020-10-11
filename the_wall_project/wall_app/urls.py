from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_wall),
    path('messages/create', views.create_message),
    path('messages/comment', views.create_comment),
    path('messages/delete', views.destroy_message),
]