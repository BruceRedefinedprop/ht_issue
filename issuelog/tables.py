import django_tables2 as tables
from django_tables2.utils import A 

from .models import Issue

        
class FeaturesTable(tables.Table):
    title = tables.LinkColumn('issue_detail', args=[A('pk')])
    class Meta:
        model = Issue
        fields = ('title', 'ht_product', 'issue_status', 'published_date','rating', 'votes')
        template_name = 'django_tables2/bootstrap.html'        

class BugsTable(tables.Table):
    title = tables.LinkColumn('issue_detail', args=[A('pk')])
    class Meta:
        model = Issue
        fields = ('title' ,'ht_product', 'issue_status', 'published_date','rating', 'votes')
        template_name = 'django_tables2/bootstrap.html'        
