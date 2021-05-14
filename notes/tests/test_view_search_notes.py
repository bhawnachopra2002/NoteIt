from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from ..models import Note
from django.db.models import Q


class AllNotesSearchTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='12test12')
        self.user1.save()
        user2 = User.objects.create_user(username='testuser2', password='12323test')
        user2.save()
        number_of_notes = 30
        for notes in range(number_of_notes):
            demo = Note.objects.create(
                user=self.user1 if notes % 2 else user2,
                title="This is Note no"+str(notes),
                content="This is a test note for user name",
                is_starred=True if notes % 3 else False
                )
            if(demo.is_starred):
                demo.tags.add("Tag1", "Tag2")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('search-notes'))
        self.assertRedirects(response, '/accounts/login/?next=/notes/search/')

    def test_logged_in_user_sees_todo_template(self):
        self.client.login(username='testuser1', password='12test12')
        url = '/notes/search/?search=Tag2'
        response = self.client.get(url)
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_note.html')

    def test_only_user_added_notes_in_list(self):
        self.client.login(username='testuser1', password='12test12')
        url = '/notes/search/?search=Tag1'
        response = self.client.get(url)
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check that initially we  have only 10 notes for first user.
        self.assertTrue('notes' in response.context)
        self.assertEqual(len(response.context['notes']), 10)
        self.assertQuerysetEqual(
            response.context['notes'],
            (Note.objects.filter(Q(user=self.user1) & ((Q(title__icontains='Tag1') | Q(tags__name__icontains='Tag1')))).distinct()),
            transform=lambda x: x)

    def test_notes_ordered_by_due_date(self):
        self.client.login(username='testuser1', password='12test12')
        url = '/notes/search/?search=Tag1'
        response = self.client.get(url)
        if 'notes' in response.context:
            notes = response.context['notes']
            # By default assertQuerysetEqual uses repr() on the first argument.
            # This is why you were having issues with the strings in the queryset comparison.
            # To work around this you can override the transform argument with a lambda function that doesn't use repr():
            self.assertQuerysetEqual(notes, (notes.order_by('-is_starred')), transform=lambda x: x)
