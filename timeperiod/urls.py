from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_timeperiods, name='timeperiod'),
    path('add/', views.add_timeperiod, name='add_timeperiod'),
    path('edit/<int:timeperiod_id>/', views.edit_timeperiod,
         name='edit_timeperiod'),
    path('delete/<int:timeperiod_id>/', views.delete_timeperiod,
         name='delete_timeperiod'),
]
