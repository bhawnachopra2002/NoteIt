from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.core.exceptions import ValidationError


def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")


# Create your models here.


class TodoTask(models.Model):  # Todolist able name that inherits models.Model
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)  # a varchar
    created = models.DateField(default=timezone.now)  # a date
    due_date = models.DateField(default=timezone.now, validators=[validate_date])  # a date
    important = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ["-due_date"]  # ordering by the due_date field

    def __str__(self):
        return self.title  # name to be shown when called
