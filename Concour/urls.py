from django.urls import path
from . import views

urlpatterns = [
    path('physique/', views.physique, name='physique'),
    path('math/', views.math, name='math'),
    path('chimie/', views.chimie, name='chimie'),
    path('detail/<int:concours_id>', views.details, name='details'),
]