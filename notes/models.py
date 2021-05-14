from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.


class Note(models.Model):
    class Meta:
        app_label = "notes"
        managed = True
        ordering = ('-is_starred',)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    is_starred = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title
