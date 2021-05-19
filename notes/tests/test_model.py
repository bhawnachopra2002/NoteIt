from django.test import TestCase
from ..models import Note
from django.contrib.auth.models import User

'''It tests the Note model being used in Notes app.'''


class NoteTest(TestCase):
    #Setup creates data to be run upon for other function in class . It creates User and Note object.
    def setUp(self):
        self.user = User.objects.create_user(username='TestUser', password='testit1212')
        self.user.save()
        self.note = Note(user=self.user, title='This is a test note')
        self.note.save()

    # Test to check if user is being set correctly for given note
    def test_read_note(self):
        self.assertEqual(self.note.user, self.user)
        self.assertEqual(self.note.title, 'This is a test note')

    # Test to check whether title is updating correctly or not
    def test_update_note_title(self):
        self.note.title = 'Updated the test title'
        self.note.save()
        self.assertEqual(self.note.title, 'Updated the test title')

    # Test to check whether is_starred field is updating correctly or not
    def test_update_note_is_starred(self):
        self.note.is_starred = True
        self.note.save()
        self.assertEqual(self.note.is_starred, True)
