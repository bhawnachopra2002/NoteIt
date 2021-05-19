from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.
''' Note model contains the essential fields and behaviors of the user notes.
    -> app_label indicates that Note model belongs to notes app
    -> ordering indicates that entries in database will be in such a way that 
       ones having is_starred field True will be on top of others .
    -> Fields :
        1. user : This will store a user objet created in our user database. 
           It will store user to which note belongs.
        2. title : It stores the title of the note . Title can have maximum of 100 characters.
        3. contents : It stores the contents of the note .
        4. is_starred : If set to True , it pins the note. By default, it is False.
        5. tags : It stores al the tags assigned to the note.
    It is used in forms.py to create new object.
    It is used in all test_views files and views.py file under notes subfolder
'''


class Note(models.Model):
    class Meta:
        app_label = "notes"
        ordering = ('-is_starred',)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    is_starred = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title
