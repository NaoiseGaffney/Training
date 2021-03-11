from django.contrib import admin
from django.urls import path
from . import views

"""
Path to:
- Home / Index Page of the Training project/website.
"""
urlpatterns = [
    path('', views.index, name='home')
]
