from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import TodoTask
from datetime import date, timedelta

'''A set of tests to check the confirm_delete_task view.'''


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
        response = self.client.get(reverse('confirm-delete-task', args=[self.task1.id]))
        self.assertRedirects(response, '/accounts/login/?next=/todo/confirm_delete/'+str(self.task1.id))

    # Test to check if user is able to access the URL correctly or not
    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='testuser1', password='12test12')
        response = self.client.get('/todo/confirm_delete/'+str(self.task1.id))
        self.assertEqual(response.status_code, 200)

    # Test to check if the correct template is being rendered at logged in user's screen
    def test_logged_in_user_sees_confirm_delete_template(self):
        self.client.login(username='testuser1', password='12test12')
        response = self.client.get(reverse('confirm-delete-task', args=[self.task1.id]))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirm_task_delete.html')
        self.assertEqual(response.context['task_detail'], self.task1)
