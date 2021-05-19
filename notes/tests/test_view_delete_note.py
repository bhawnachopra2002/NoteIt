from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Note

'''A set of tests to check the delete_note view.'''


class NotesDeleteTest(TestCase):

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
        response = self.client.get(reverse('delete-note', args=[self.note1.id]))
        self.assertRedirects(response, '/accounts/login/?next=/notes/delete/'+str(self.note1.id))

    # Test to check if delete-note urlredirects to view-all-notes view. 
    def test_delete_url_redirects_at_desired_location(self):
        self.client.login(username='testuser1', password='12test12')
        response = self.client.get('/notes/delete/'+str(self.note1.id))
        self.assertRedirects(response, "/notes/view_all/")
