from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_timeperiods, name='timeperiod'),
    path('<int:timeperiod_id>/', views.timeperiod_detail,
         name='timeperiod_detail'),
    path('add/', views.add_timeperiod, name='add_timeperiod'),
    path('edit/<int:timeperiod_id>/', views.edit_timeperiod,
         name='edit_timeperiod'),
]
