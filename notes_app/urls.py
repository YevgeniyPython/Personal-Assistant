from django.urls import path
from . import views

urlpatterns = [
    # path('', views.note_home, name='note_home'),
    path('', views.note_list, name='note_list'),
    path('add/', views.add_note, name='add_note'),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('<int:note_id>/', views.note_detail, name='note_detail'),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('tag_list/', views.tag_list, name='tag_list'),
    path('tag_list/delete/<int:tag_id>/', views.delete_tag, name='delete_tag')
]
