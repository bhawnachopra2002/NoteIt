from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import TodoTask
from datetime import date, timedelta

'''A set of tests to check the delete_task view.'''


class AllTodoViewTest(TestCase):
    # Setup to define test data
    def setUp(self):
        user1 = User.objects.create_user(username='testuser1', password='12test12')
        user1.save()
        self.task1 = TodoTask.objects.create(
                user=user1,
                title="This is test task",
                created=date.today(),
                due_date=date.today()+timedelta(days=5),
                important=True
                )
        self.task1.tags.add("Tag1", "Tag2")

    # Test to check if redirects are working or not in case where user is not logged in.
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('delete-task', args=[self.task1.id]))
        self.assertRedirects(response, '/accounts/login/?next=/todo/delete/'+str(self.task1.id))

    # Test to check if delete-note urlredirects to view-all-notes view. 
    def test_delete_url_redirects_at_desired_location(self):
        self.client.login(username='testuser1', password='12test12')
        response = self.client.get('/todo/delete/'+str(self.task1.id))
        self.assertRedirects(response, '/todo/view_all/')
