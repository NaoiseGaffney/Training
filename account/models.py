from django.db import models
from django.conf import settings
from orders.models import Order


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=80, blank=True, null=True)
    post_code = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)


    def __str__(self):
        return f'Profile for user {self.user.username}'


class Comment(models.Model):
    CHOICES = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ForeignKey(Order, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=CHOICES)
    comment = models.CharField(max_length=250, blank=True, null=True)
