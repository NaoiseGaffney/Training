from django.db import models
from django.conf import settings
from orders.models import Order


"""
Models for the Character Profile and Comment/Rating of Courses/Coaching Sessions.
- Profile, used for the Character Profile.
- Comment, used for the Comment and Rating of Courses/Coaching Sessions.
"""


class Profile(models.Model):
    """
    Character Profile model used by forms and views to allow the user to edit/update the Character Profile.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    address = models.CharField(max_length=80, blank=True, null=True)
    post_code = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
