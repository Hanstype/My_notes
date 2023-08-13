from django.urls import path
from . import views


urlpatterns = [
    path('',views.getRoutes, name ='routes'),
    path('notes/',views.get_notes, name='notes'),
    path('notes/create', views.createNote, name='create-note'),
    path('notes/<int:post_id>/update',views.updateNote, name='update-note'),
    path('notes/<int:post_id>/delete',views.deleteNote, name='delete-note'),
    path('notes/<int:post_id>',views.get_note, name='note'),
]
