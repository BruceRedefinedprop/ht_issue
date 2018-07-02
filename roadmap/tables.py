import django_tables2 as tables
from .models import Roadmap
from issuelog.models import Issue

"""
create helper classes for django_tables2 to defined product Roadmap
tables.  the Roadmap table shows product release schedule and TopIssuesTable
shows top features or bug fixes requested.   

"""

class RoadmapTable(tables.Table):
    class Meta:
        model = Roadmap
        fields = ('release_num', 'title', 'releases_date', 'content')
        template_name = 'django_tables2/bootstrap.html'
        
class TopIssuesTable(tables.Table):
    class Meta:
        model = Issue
        fields = ('title', 'ht_product', 'rating', 'votes')
        template_name = 'django_tables2/bootstrap.html'        
