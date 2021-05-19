from django.test import TestCase
from ..models import TodoTask
from django.contrib.auth.models import User
from datetime import date, timedelta

'''It tests the TodoTask model being used in todo app.'''


class TaskTest(TestCase):
    #Setup creates data to be run upon for other function in class . It creates User and TodoTask object.
    def setUp(self):
        self.user = User.objects.create_user(username='TestUser', password='testit1212')
        self.user.save()
        self.timestamp = date.today()
        self.task = TodoTask(
            user=self.user,
            title='This is a test task',
            due_date=self.timestamp-timedelta(days=2))
        self.task.save()

    # Test to check if user is being set correctly for given task
    def test_read_task(self):
        self.assertEqual(self.task.user, self.user)
        self.assertEqual(self.task.title, 'This is a test task')

    # Test to check whether title is updating correctly or not
    def test_update_task_title(self):
        self.task.title = 'Updated the test title'
        self.task.save()
        self.assertEqual(self.task.title, 'Updated the test title')

    # Test to check whether due_date field is updating correctly or not
    def test_update_task_due(self):
        self.task.due_date = self.timestamp + timedelta(days=2)
        self.task.save()
        self.assertEqual(self.task.due_date, self.timestamp + timedelta(days=2))

    # Test to check whether important field is updating correctly or not
    def test_update_task_important(self):
        self.task.important = True
        self.task.save()
        self.assertEqual(self.task.important, True)
