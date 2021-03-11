from django.contrib import admin
from .models import Profile


"""
Admin Views displaying additional fields, and adding a search field for
CommentAdmin.
"""


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'post_code', 'city']
