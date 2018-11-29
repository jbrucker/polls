import django.test
from django.urls import reverse

class PollRequestsTest(django.test.TestCase):

    def test_get_question(self):
        """
        Get a valid question (requires some initial data)
        """
        response = self.client.get(reverse('polls:detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        
    def test_get_nonexisting_question(self):
        """
        If request for non-existing question, redirect to polls index, not 404 response.
        """
        response = self.client.get(reverse('polls:detail', args=[9999999]))
        self.assertEqual(response.status_code, 303)

    def test_get_invalid_question_id(self):
        """
        If the question id is invalid, it returns a 404 ?
        TODO: Should really be 400 BAD REQUEST.
        """
        response = self.client.get('/polls/3b/')
        self.assertEqual(response.status_code, 404)