from django.db import models
from django.utils import timezone

# Create your models here.
class Productmgr(models.Model):
    mgr = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    
    def __str__(self):
        return self.mgr

class Roadmap(models.Model):
    prod_mgr = models.ForeignKey(Productmgr)
    release_num = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True)
    releases_date = models.DateField(blank=True, null=True, default=timezone.now)
    
    def __str__(self):
        return "{0}-rel: {1}-Launch Date: {2}".format(self.title, self.release_num, self.releases_date)
    
