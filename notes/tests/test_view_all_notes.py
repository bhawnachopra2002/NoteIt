from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Note


class AllNotesViewTest(TestCase):

    def setUp(self):
        user1 = User.objects.create_user(username='testuser1', password='12test12')
        user1.save()
        user2 = User.objects.create_user(username='testuser2', password='12323test')
        user2.save()
        number_of_notes = 30
        for notes in range(number_of_notes):
            demo = Note.objects.create(
                user=user1 if notes % 2 else user2,
                title="This is Note no"+str(notes),
                content="This is a test note for user name",
                is_starred=True if notes % 3 else False
                )
            if(demo.is_starred):
                demo.tags.add("Tag1", "Tag2")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('view-all-notes'))
        self.assertRedirects(response, '/accounts/login/?next=/notes/view_all/')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='testuser1', password='12test12')
        response = self.client.get('/notes/view_all/')
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_sees_notes_template(self):
        self.client.login(username='testuser1', password='12test12')
        response = self.client.get(reverse('view-all-notes'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_all_notes.html')

    def test_only_user_added_notes_in_list(self):
        self.client.login(username='testuser1', password='12test12')
        response = self.client.get(reverse('view-all-notes'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check that initially we  have only 15 notes for first user.
        self.assertTrue('notes' in response.context)
        self.assertEqual(len(response.context['notes']), 15)
        for note in response.context['notes']:
            self.assertEqual(note.user.username, 'testuser1')

    def test_notes_ordered_by_is_starred(self):
        self.client.login(username='testuser1', password='12test12')
        response = self.client.get(reverse('view-all-notes'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        notes = response.context['notes']
        # By default assertQuerysetEqual uses repr() on the first argument.
        # This is why you were having issues with the strings in the queryset comparison.
        # To work around this you can override the transform argument with a lambda function that doesn't use repr()
        self.assertQuerysetEqual(notes, (notes.order_by('-is_starred')), transform=lambda x: x)
