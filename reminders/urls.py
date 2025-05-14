from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminder_list, name='reminder_list'),
    path('add/', views.create_reminder, name='create_reminder'),
    path('success/', views.reminder_success, name='reminder_success'),
    path('api/create/', views.api_create_reminder, name='api_create_reminder'),
]
