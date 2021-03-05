from django.contrib import admin
from .models import Profile, Comment


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'post_code', 'city']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'orders', 'rating']
    search_fields = ('rating', 'comment')