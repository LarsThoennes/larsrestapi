from collections import UserDict
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    created_at = models.DateField(("Date"), default=timezone.now)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )