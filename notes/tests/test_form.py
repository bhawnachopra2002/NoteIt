from ..forms import AddNoteForm
from django.test import TestCase
# Create your tests here.


class AddnoteFormTest(TestCase):
    def test_add_note_title_isempty(self):
        form = AddNoteForm(data={'title': ""})
        self.assertFalse(form.is_valid())

    def test_add_note_title_maxlength(self):
        form = AddNoteForm(data={'title': 'x' * 101})
        self.assertFalse(form.is_valid())
