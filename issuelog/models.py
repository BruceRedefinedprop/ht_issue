from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from choices import ISSUE_TAG_CHOICES, ISSUE_STATUS_CHOICES, PRODUCT_CHOICES

# Create your models here.

class Issue(models.Model):
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
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True)
    published_date = models.DateField(blank=True, null=True, default=timezone.now)
    votes = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    tag = models.CharField(max_length=10, choices=ISSUE_TAG_CHOICES, default="bug")
    image = models.ImageField(upload_to="img", blank=True, null=True)
    tag_edit = models.BooleanField(default=True)
    content_edit = models.BooleanField(default=True)
    issue_status = models.CharField(max_length=10, choices=ISSUE_STATUS_CHOICES, default="open")
    ht_product = models.CharField(max_length=15, choices=PRODUCT_CHOICES, default="other")
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.title, self.tag, self.issue_status)
        
    
class Comment(models.Model):
    """
    A single comment.   A Post has a one-to-many relationship with comments.  
    Also may also have one-to-many relationship with comments.
    """
    author = models.ForeignKey('auth.User')
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_created_data = models.DateTimeField(auto_now_add=True)
    voted = models.BooleanField(default=False)
    rating = models.IntegerField(
        default=0,
        validators = [MaxValueValidator(5), MinValueValidator(0)] 
    )

    def __str__(self):
        return self.comment