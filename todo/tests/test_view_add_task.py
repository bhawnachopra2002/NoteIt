from ..forms import AddTaskForm
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import TodoTask
from datetime import date, timedelta


class AllTodoViewTest(TestCase):

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

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('add-task'))
        self.assertRedirects(response, '/accounts/login/?next=/todo/add/')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='testuser1', password='12test12')
        response = self.client.get('/todo/add/')
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_sees_correct_form(self):
        self.client.login(username='testuser1', password='12test12')
        response = self.client.get(reverse('add-task'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], AddTaskForm)
