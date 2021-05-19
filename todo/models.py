from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.core.exceptions import ValidationError

''' TodoTask model contains the essential fields and behaviors of the user notes.

    -> ordering indicates that entries in database will be in such a way that 
       ones having due_date field in future will be on top of others .
    -> Fields :
        1. user : This will store a user objet created in our user database. 
           It will store user to which task belongs.
        2. title : It stores the title of the task . Title can have maximum of 250 characters.
        3. created : It stores the date on which task was created. It cannot be modified by user.
        4. due_date : It stores the date on which task is due to be completed .Due date is validated before saving the object . 
                      The criteria is that due date must not be a past date
        5. important : If set to True , it amrks the task as important. By default, it is False.
        6. tags : It stores all the tags assigned to the task.
    It is used in forms.py to create new object.
    It is used in all test_views files and views.py file under todo subfolder
'''
# Validation function : It takes input as date and raises validation error if date is lesser than current date
def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")

class TodoTask(models.Model):
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
