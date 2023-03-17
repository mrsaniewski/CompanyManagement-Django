from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from sqlalchemy import func


class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    complete = models.BooleanField()

    def __str__(self):
        return self.text


class Prize(models.Model):
    prizes = models.ForeignKey(User, on_delete=models.CASCADE, related_name="prizes")
    prizename = models.CharField(max_length=150)
    value = models.IntegerField(default=0)
    claimed = models.BooleanField(default=False)

    def __str__(self):
        return self.prizename