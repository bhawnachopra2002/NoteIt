from django import forms
from .models import Note
from django.utils.translation import ugettext_lazy as _


class AddNoteForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Note

        # specify fields to be used
        fields = [
            "title",
            "content",
            "is_starred",
            "tags",
        ]
        labels = {
            "is_starred": _('Important'),
        }
