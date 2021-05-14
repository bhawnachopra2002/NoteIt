from ..forms import AddTaskForm
from django.test import TestCase
from datetime import date, timedelta


class AddTaskFormTest(TestCase):
    def test_add_task_title_isempty(self):
        form = AddTaskForm(data={'title': ""})
        self.assertFalse(form.is_valid())

    def test_add_task_title_maxlength(self):
        form = AddTaskForm(data={'title': 'x' * 252})
        self.assertFalse(form.is_valid())

    def test_add_task_duedate_widget(self):
        form = AddTaskForm()
        self.assertTrue(form.fields['due_date'].widget.__class__.__name__ == 'DateInput')

    def test_add_task_duedate_field_help_text(self):
        form = AddTaskForm()
        self.assertEqual(form.fields['due_date'].help_text, 'Do not enter past dates')

    def test_add_task_duedate_in_past(self):
        due = date.today() - timedelta(days=3)
        form = AddTaskForm(data={'title': 'test task', 'due_date': due})
        self.assertFalse(form.is_valid())

    def test__add_task_duedate_today(self):
        due = date.today()
        form = AddTaskForm(data={'title': 'test task', 'due_date': due})
        self.assertTrue(form.is_valid())

    def test_add_task_duedate_future(self):
        due = date.today() + timedelta(weeks=4)
        form = AddTaskForm(data={'title': 'test task', 'due_date': due})
        self.assertTrue(form.is_valid())
