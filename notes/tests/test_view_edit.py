from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Note
from ..forms import AddNoteForm

'''A set of tests to check the update_note_view.'''


class NotesUpdateTest(TestCase):

    # Setup to define test data
    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='12test12')
        self.user1.save()
        self.note1 = Note.objects.create(
            user=self.user1,
            title="This is a test note",
            content="This is a test note for user name",
            is_starred=True
            )
        self.note1.tags.add("Tag test", "Tag1", "Tag2")

    # Test to check if redirects are working or not in case where user is not logged in.
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('update-note', args=[self.note1.id]))
        self.assertRedirects(response, '/accounts/login/?next=/notes/update/'+str(self.note1.id))

    # Test to check if user is able to access the URL correctly or not
    def test_edit_url_exists_at_desired_location(self):
        self.client.login(username='testuser1', password='12test12')
        response = self.client.get('/notes/update/'+str(self.note1.id))
        self.assertEqual(response.status_code, 200)

    # Test to check if the correct template is being rendered at logged in user's screen
    def test_logged_in_user_sees_edit_notes_template(self):
        self.client.login(username='testuser1', password='12test12')
        response = self.client.get(reverse('update-note', args=[self.note1.id]))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_note.html')
        self.assertIsInstance(response.context['form'], AddNoteForm)
