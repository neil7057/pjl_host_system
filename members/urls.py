from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_members, name='members'),
    path('<int:members_id>/', views.members_detail, name='members_detail'),
    path('add/', views.add_members, name='add_members'),
    path('edit/<int:members_id>/', views.edit_members, name='edit_members'),
    path('delete/<int:members_id>/', views.delete_members,
         name='delete_members'),
]
