import unittest
from django.test import Client, TestCase
from .models import Issue, Comment

# class GetIssueTest(unittest.TestCase):
#     def setUp(self):
#         # Every test needs a client.
#         self.client = Client()

#     def test_details(self):
#         # Issue a GET request.
#         response = self.client.get('/issue')

#         # Check that the response is 200 OK.
#         self.assertEqual(response.status_code, 200)

# class ViewTests(TestCase):
#     def test1(self):
#         issues = Issue.objects.exclude(issue_status = "closed").order_by('-published_date')
#         self.assertIs(issues.count(), 10)
        