from django import forms
from .models import TodoTask
from django.utils.translation import ugettext_lazy as _


class DateInput(forms.DateInput):
    input_type = 'date'


class AddTaskForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = TodoTask

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
