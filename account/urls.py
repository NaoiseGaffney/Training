from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

"""
Paths to the:
- default Account URL '' referred to '/account/login/'
- the register new user URL 'register/'
- the edit character profile URL 'edit/'
- the character dashboard after a successful login 'dashboard/'
"""
urlpatterns = [
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'),
    path(
        '',
        include('django.contrib.auth.urls')),
    path(
        'register/',
        views.register,
        name='register'),
    path(
        'edit/',
        views.edit,
        name='edit'),
    path(
        'comment_edit/<comment_id>',
        views.comment_edit,
        name='comment_edit'),
    path(
        'comment_delete/<comment_id>',
        views.comment_delete,
        name='comment_delete'),
]
