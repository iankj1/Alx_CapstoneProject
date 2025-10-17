from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    streak_count = models.IntegerField(default=0)
    last_task_completed_date = models.DateField(null=True, blank=True)

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
