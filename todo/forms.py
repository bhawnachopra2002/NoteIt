from django import forms
from .models import TodoTask
from django.utils.translation import ugettext_lazy as _

'''Form to Add and update the tasks . It is used to update the TodoTask model in the database.
Contents of fields variable contain the data columns to be displayed in the form.
help_texts contain corresponding text for various fields as helper texts to help user provide correct input.
It is used in Add task and Update task functions in views.py file under todos subfolder.
The corresponding tests are written in test_form.py file under tests subfolder in todo subfolder.'''

# This class is defined to make input for due_date field to be DateInput provided by django forms.
class DateInput(forms.DateInput):
    input_type = 'date'

class AddTaskForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = TodoTask
        # Specify type of input widget to be used.
        widgets = {
            'due_date': DateInput}

        # specify fields to be used
        fields = [
            "title",
            "due_date",
            "important",
            "tags"
        ]
        help_texts = {
            "due_date": _('Do not enter past dates'),
        }
