from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from ..models import TodoTask
from datetime import date, timedelta
from django.db.models import Q


class AllTodoSearchTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='12test12')
        self.user1.save()
        user2 = User.objects.create_user(username='testuser2', password='12323test')
        user2.save()
        number_of_todos = 30
        for todos in range(number_of_todos):
            demo = TodoTask.objects.create(
                user=self.user1 if todos % 2 else user2,
                title="This is task no"+str(todos),
                created=date.today(),
                due_date=date.today()+timedelta(days=todos),
                important=True if todos % 3 else False
                )
            if(demo.important):
                demo.tags.add("Tag1", "Tag2")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('search-tasks'))
        self.assertRedirects(response, '/accounts/login/?next=/todo/search/')

    def test_logged_in_user_sees_todo_template(self):
        self.client.login(username='testuser1', password='12test12')
        url = '/todo/search/?search=Tag1'
        response = self.client.get(url)
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_task.html')

    def test_only_user_added_tasks_in_list(self):
        self.client.login(username='testuser1', password='12test12')
        url = '/todo/search/?search=Tag1'
        response = self.client.get(url)
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check that initially we  have only 10 tasks for first user.
        self.assertTrue('tasks' in response.context)
        self.assertEqual(len(response.context['tasks']), 10)
        self.assertQuerysetEqual(
            response.context['tasks'],
            (TodoTask.objects.filter(Q(user=self.user1) & ((Q(title__icontains='Tag1') | Q(tags__name__icontains='Tag1')))).distinct()),
            transform=lambda x: x)

    def test_tasks_ordered_by_due_date(self):
        self.client.login(username='testuser1', password='12test12')
        url = '/todo/search/?search=Tag1'
        response = self.client.get(url)
        if 'tasks' in response.context:
            tasks = response.context['tasks']
            # By default assertQuerysetEqual uses repr() on the first argument.
            # This is why you were having issues with the strings in the queryset comparison.
            # To work around this you can override the transform argument with a lambda function that doesn't use repr():
            self.assertQuerysetEqual(tasks, (tasks.order_by('-due_date')), transform=lambda x: x)
