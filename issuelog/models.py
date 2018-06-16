from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    """
    Defines a single issue post.
    tag defines if this is an issue or bug
    Title of issues
    content - detials of issue or bug
    created date defines when the bug / issues was created
    published_date is when issue / bug was published_date
    votes are number of unique votes
    weighted_votes - each vote is rated 0 of not important to 5 for very important
    tag_edit and content_edit are flags that define if can be edited.  
       if issue is pending or closed, not editing is allowed.
    post_status defined if an bug or issue is open, pending revision or closed.
    
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    votes = models.IntegerField(default=0)
    weighted_votes = models.IntegerField(default=0)
    tag = models.CharField(max_length=10)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    tag_edit = models.BooleanField(default=True)
    content_edit = models.BooleanField(default=True)
    post_status = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.Title
    