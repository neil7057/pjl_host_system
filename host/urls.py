from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_hosts, name='hosts'),
    path('<int:host_id>/', views.host_detail, name='host_detail'),
    path('add/', views.add_host, name='add_host'),
    path('edit/<int:host_id>/', views.edit_host, name='edit_host'),
]
