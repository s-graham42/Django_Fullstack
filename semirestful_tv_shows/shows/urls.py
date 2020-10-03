from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # redirect
    path('shows', views.shows), # template
    path('shows/new', views.new), # template
    path('shows/create', views.create), # method, redirect
    path('shows/<int:show_id>', views.one_show), # template
    path('shows/<int:show_id>/edit', views.edit), # template
    path('shows/<int:show_id>/update', views.update), # method, redirect
    path('shows/<int:show_id>/destroy', views.destroy), # method, redirect
]