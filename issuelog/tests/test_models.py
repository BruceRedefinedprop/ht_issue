import unittest
from django.test import  TestCase, Client
from issuelog.models import Issue, Comment
from django.contrib.auth.models import User
from django.utils import timezone
from choices import ISSUE_TAG_CHOICES, ISSUE_STATUS_CHOICES, PRODUCT_CHOICES

class IssueModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        """
        Set up text to verify the models are set up correctly,
        checking option settings and implicently creating and retrieving 
        an object.   Other records were tested using inspection, since
        the application basically records and display database records.
        """
        #Set up non-modified objects used by all test methods
        # No client is required, but you can see code where 
        # creating user and then logging that user into the system.
        # cls.client = Client()
        # Create a user
        user = User.objects.create(username='test')
        user.set_password('test1234')
        user.save()
        # logedin = cls.client.login(username='test', password='test1234')
        #create an test issue
        Issue.objects.create(title="test 1", author = user, 
            issue_status = "closed")
            
    def test_title_label(self):
        issue=Issue.objects.get(id=1)
        field_label = issue.title
        self.assertEquals(field_label,'test 1')
        max_length = issue._meta.get_field('title').max_length
        self.assertEquals(max_length,200)

    def test_content_label(self):
        issue=Issue.objects.get(id=1)
        field1 = issue._meta.get_field('content').blank
        self.assertEquals(field1,True)
        
    def test_createddate_label(self):
        issue=Issue.objects.get(id=1)
        field1 = issue._meta.get_field('created_date').auto_now_add
        self.assertEquals(field1,True)
        
    def test_pubddate_label(self):
        issue=Issue.objects.get(id=1)
        field1 = issue._meta.get_field('published_date').blank
        self.assertEquals(field1,True)    
        field2 = issue._meta.get_field('published_date').null
        self.assertEquals(field2,True)  
        field3 = issue._meta.get_field('published_date').default
        self.assertEquals(field3, timezone.now) 
        
    def test_votes_label(self):
        issue=Issue.objects.get(id=1)
        field3 = issue._meta.get_field('votes').default
        self.assertEquals(field3, 0) 
        
    def test_rate_label(self):
        issue=Issue.objects.get(id=1)
        field1 = issue._meta.get_field('rating').max_digits
        self.assertEquals(field1,4)    
        field2 = issue._meta.get_field('rating').decimal_places
        self.assertEquals(field2, 1)  
        field3 = issue._meta.get_field('rating').default
        self.assertEquals(field3, 0) 
        
    def test_tag_label(self):
        issue=Issue.objects.get(id=1)
        field1 = issue._meta.get_field('tag').max_length
        self.assertEquals(field1,10)    
        field2 = issue._meta.get_field('tag').choices
        self.assertEquals(field2,ISSUE_TAG_CHOICES)  
        field3 = issue._meta.get_field('tag').default
        self.assertEquals(field3, "bug")  
        
    def test_issuestatus_label(self):
        issue=Issue.objects.get(id=1)
        field1 = issue._meta.get_field('issue_status').max_length
        self.assertEquals(field1,10)    
        field2 = issue._meta.get_field('issue_status').choices
        self.assertEquals(field2,ISSUE_STATUS_CHOICES)  
        field3 = issue._meta.get_field('issue_status').default
        self.assertEquals(field3, "open")   
        
    def test_htproduct_label(self):
        issue=Issue.objects.get(id=1)
        field1 = issue._meta.get_field('ht_product').max_length
        self.assertEquals(field1,15)    
        field2 = issue._meta.get_field('ht_product').choices
        self.assertEquals(field2,PRODUCT_CHOICES)  
        field3 = issue._meta.get_field('ht_product').default
        self.assertEquals(field3, "other")      
    
class CommentModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Create user to add to a Comment
        user = User.objects.create(username='test')
        user.set_password('test1234')
        user.save()
        #create an issue to add to Comment
        Issue.objects.create(title="test 1", author = user, 
            issue_status = "closed")  
        # get an issue and create a comment    
        issue=Issue.objects.get(id=1)   
        Comment.objects.create(author=user, issue=issue, comment="test comment")  
        
        
    #test option and label settings    
    def test_content_label(self):
        issue=Issue.objects.get(id=1) 
        comment=Comment.objects.get(issue=issue)
        field1 = comment.author
        self.assertEquals(field1,issue.author)
        
    def test_createddate_label(self):
        issue=Issue.objects.get(id=1) 
        comment=Comment.objects.get(issue=issue)
        field1 = issue._meta.get_field('created_date').auto_now_add
        self.assertEquals(field1,True)  
        
    def test_failrate_label(self):
        issue=Issue.objects.get(id=1)
        
        field3 = issue._meta.get_field('rating').default
        self.assertEquals(field3, 1)     
        
    def test_rate_label(self):
        issue=Issue.objects.get(id=1)
        
        field3 = issue._meta.get_field('rating').default
        self.assertEquals(field3, 0)     
        
        
