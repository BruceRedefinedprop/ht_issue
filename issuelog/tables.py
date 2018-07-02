import django_tables2 as tables
from django_tables2.utils import A 

from .models import Issue

"""
Defines tables to displayed on Feedback pages (issueposts.html).
These tables rely on the functionality of django_tables2 and is configured
to be sortable by default.  They are formated using bootstrap3.

django_tables2 is dependent on Bootstrap 3.

"""

# defined feature table.
# title column is linked to issue_detail page, to access click on title.
class FeaturesTable(tables.Table):
    title = tables.LinkColumn('issue_detail', args=[A('pk')])
    class Meta:
        model = Issue
        fields = ('title', 'ht_product', 'issue_status', 'published_date','rating', 'votes')
        template_name = 'django_tables2/bootstrap.html'        

# defined bug fix required table.  Likewise, title is linked to issue detail page.
class BugsTable(tables.Table):
    title = tables.LinkColumn('issue_detail', args=[A('pk')])
    class Meta:
        model = Issue
        fields = ('title' ,'ht_product', 'issue_status', 'published_date','rating', 'votes')
        template_name = 'django_tables2/bootstrap.html'        
