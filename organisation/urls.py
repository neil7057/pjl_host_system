from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_organisations, name='organisation'),
    path('<int:organisation_id>/', views.organisation_detail,
         name='organisation_detail'),
    path('add/', views.add_organisation, name='add_organisation'),
    path('edit/<int:organisation_id>/', views.edit_organisation,
         name='edit_organisation'),
    path('delete/<int:organisation_id>/', views.delete_organisation,
         name='delete_organisation'),
]
