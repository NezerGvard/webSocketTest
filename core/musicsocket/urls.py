from django.urls import path
from . import views

urlpatterns = [
    path('',  views.Music.as_view()),
]