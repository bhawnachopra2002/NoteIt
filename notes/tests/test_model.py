from django.test import TestCase
from ..models import Note
from django.contrib.auth.models import User
# Create your tests here.


class NoteTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='TestUser', password='testit1212')
        self.user.save()
        self.note = Note(user=self.user, title='This is a test note')
        self.note.save()

    def test_read_note(self):
        self.assertEqual(self.note.user, self.user)
        self.assertEqual(self.note.title, 'This is a test note')

    def test_update_note_title(self):
        self.note.title = 'Updated the test title'
        self.note.save()
        self.assertEqual(self.note.title, 'Updated the test title')

    def test_update_note_is_starred(self):
        self.note.is_starred = True
        self.note.save()
        self.assertEqual(self.note.is_starred, True)
