from django.urls import path
from . import views

urlpatterns = [
    path('', views.management, name='management'),
    path(
        'toggle/<int:message_id>/',
        views.toggle_message,
        name='toggle_message'
    ),
    path('contact_us', views.contact_us, name='contact_us'),

]
