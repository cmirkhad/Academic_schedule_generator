from django.urls import path
from .views import generate_schedule

urlpatterns = [
    path('generate_schedule/', generate_schedule, name='generate_schedule'),
]
