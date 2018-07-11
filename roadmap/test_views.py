import unittest
from django.test import Client, TestCase
from django.contrib import messages, auth
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse
from roadmap.models import Productmgr, Roadmap
from django.contrib.auth.models import User

class GetRoadmapTest(TestCase):
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
        
    def test_getroadmappage_fail(self):
        # Designed to fail. Requires login to access
        response = self.client.get('/roadmap')
        # Should be 301, redirect page.
        self.assertEqual(response.status_code, 200)   
        #redirect to login page.
        self.assertRedirects(response, "accounts/login/?next=/issue/")    
        
    def test_getroadmappage(self):
        # Requires log in to reach page
        logedin = self.client.login(username='test', password='test1234')
        
        response = self.client.get(reverse('roadmap'))
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        #check right template
        self.assertTemplateUsed(response, 'roadmap/roadmap.html', 'base.html')    