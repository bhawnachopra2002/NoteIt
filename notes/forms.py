from django import forms
from .models import Note
from django.utils.translation import ugettext_lazy as _

'''Form to Add and update the notes . It is used to update the notes model in the database.
Contents of fields variable contain the data columns to be displayed in the form.
It is used in Add note and Update note functions in views.py file under notes subfolder.
The corresponding tests are written in test_form.py file under tests subfolder in notes subfolder.'''

class AddNoteForm(forms.ModelForm):

    class Meta:
        model = Note

        fields = [
            "title",
            "content",
            "is_starred",
            "tags",
        ]
        # Renamed label corresponding to is_starred attribute to Important
        labels = {
            "is_starred": _('Important'),
        }
