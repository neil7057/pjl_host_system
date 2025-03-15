from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_pupils, name='pupils'),
    path('<int:pupil_id>/', views.pupil_detail, name='pupil_detail'),
    path('add/', views.add_pupil, name='add_pupil'),
    path('edit/<int:pupil_id>/', views.edit_pupil, name='edit_pupil'),
    path('delete/<int:pupil_id>/', views.delete_pupil,
         name='delete_pupil'),
]
