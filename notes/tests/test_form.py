from ..forms import AddNoteForm
from django.test import TestCase

''' It contains tests for forms used in Notes app.'''


class AddnoteFormTest(TestCase):
    # Test of whether an empty title is accepted or not
    def test_add_note_title_isempty(self):
        form = AddNoteForm(data={'title': ""})
        self.assertFalse(form.is_valid())
        
    # Test of whether a title exceeding max-length characters is accepted or not.
    def test_add_note_title_maxlength(self):
        form = AddNoteForm(data={'title': 'x' * 101})
        self.assertFalse(form.is_valid())
