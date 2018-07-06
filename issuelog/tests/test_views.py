import unittest
from django.test import Client, TestCase
from django.contrib import messages, auth
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse
from issuelog.models import Issue, Comment
from django.contrib.auth.models import User
from issuelog.forms import IssuePostForm

class GetIssueTest(TestCase):
    """
    Tests get issue view, by setting up user and testing if the page
    can be reached without logging in (should fail), with logging in and if the
    correct template is served.  Also verify that when no loggon is present, that 
    user is redirected to the login page.
    
    """
    def setUp(self):
        self.client = Client()
        user = User.objects.create(username='test')
        user.set_password('test1234')
        user.save()
        
    
    def test_getissuepage_fail(self):
        # Designed to fail. Requires login to access
        response = self.client.get('/issue')
        # Should be 301, redirect page.
        self.assertEqual(response.status_code, 200)   
        #redirect to login page.
        self.assertRedirects(response, "accounts/login/?next=/issue/")
        
    def test_getissuepage(self):
        # Requires log in to reach page
        logedin = self.client.login(username='test', password='test1234')
        print("log in worked? ", logedin)
        response = self.client.get(reverse('get_issues'))
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        #check right template
        self.assertTemplateUsed(response, 'issuelog/issueposts.html', 'base.html')

class UserFormTest(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create(username='test')
        user.set_password('test1234')
        user.save()
        Issue.objects.create(title="test 1", author = user, 
            issue_status = "open")

    def test_issueform_valid(self):
        logedin = self.client.login(username='test', password='test1234')
        issue=Issue.objects.get(id=1)
        form = IssuePostForm(data = {'title': issue.title, 'content': issue.content, 'published_date': issue.published_date, 'tag' : issue.tag, 'image': issue.image, 'ht_product': issue.ht_product}, instance=issue)
        self.assertTrue(form.is_valid())

        
      