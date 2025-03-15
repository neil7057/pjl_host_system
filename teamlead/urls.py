from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_teamleads, name='teamlead'),
    path('add/', views.add_teamlead, name='add_teamlead'),
    path('edit/<int:teamlead_id>/', views.edit_teamlead, name='edit_teamlead'),
    path('delete/<int:teamlead_id>/', views.delete_teamlead,
         name='delete_teamlead'),
]
