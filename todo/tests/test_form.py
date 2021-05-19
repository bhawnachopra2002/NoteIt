from ..forms import AddTaskForm
from django.test import TestCase
from datetime import date, timedelta

''' It contains tests for forms used in Todo app.'''

class AddTaskFormTest(TestCase):
    # Test of whether an empty title is accepted or not
    def test_add_task_title_isempty(self):
        form = AddTaskForm(data={'title': ""})
        self.assertFalse(form.is_valid())

    # Test of whether a title exceeding max-length characters is accepted or not.
    def test_add_task_title_maxlength(self):
        form = AddTaskForm(data={'title': 'x' * 252})
        self.assertFalse(form.is_valid())

    # Test of whether Date widget is appearing for due_date field on form or not.
    def test_add_task_duedate_widget(self):
        form = AddTaskForm()
        self.assertTrue(form.fields['due_date'].widget.__class__.__name__ == 'DateInput')

    # Test of whether help text is appearing for due_date field on form or not.
    def test_add_task_duedate_field_help_text(self):
        form = AddTaskForm()
        self.assertEqual(form.fields['due_date'].help_text, 'Do not enter past dates')

    '''Test of whether date in past is being accepted for due_date field on form or not.It has 3 cases.
    test_add_task_duedate_in_past has input of 3 days before current date and is expected to assert False as output
    test__add_task_duedate_today has input of date as current date and is expected to assert True as output
    test__add_task_duedate_future has input of date as 4 weeks after current date and is expected to assert True as output
    '''
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
