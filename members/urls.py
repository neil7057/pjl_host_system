from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_members, name='members'),
    path('<int:members_id>/', views.member_detail, name='member_detail'),
    path('add/', views.add_member, name='add_member'),
    path('edit/<int:members_id>/', views.edit_member, name='edit_member'),
    path('delete/<int:members_id>/', views.delete_member,
         name='delete_member'),
]
