from django.test import TestCase

'''A set of tests to check the sign_up view.'''
# Create your tests here.
class SignUpTest(TestCase):
    # Test to check if user is able to access the URL correctly or not
    def test_signup_url_exists_at_desired_location(self):
        response = self.client.get('/accounts/sign_up/')
        self.assertEquals(response.status_code, 200)
    
    def test_signup_url_redirects_at_desired_location(self):
        data = {
            'username': 'testuser',
            'password1': 'shinchannohara',
            'password2': 'shinchannohara',
        }
        response = self.client.post('/accounts/sign_up/',data)
        self.assertRedirects(response, "/notes/view_all/")