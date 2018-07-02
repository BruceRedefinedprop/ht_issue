from django.conf.urls import url
from .views import get_issues, issue_detail, create_or_edit_issue, create_or_edit_comment, del_comment

"""
Sets up URLs for issue / feedback functions.

get_issues creates a master list of feature and bug fix requests

issue_detail shows the detail of issue as well as list of comments

create_or_edit_issue and create_or_edit_comment provide forms documenting
new issues or edit existing ones.  it use pk or primary key to retrieve the issue detial,

del_comment lets only the author to delete a comment.

"""



urlpatterns = [
    url(r'^$', get_issues, name='get_issues'),
    url(r'^(?P<pk>\d+)/$', issue_detail, name='issue_detail'),
    url(r'^new/$', create_or_edit_issue, name='new_issue'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_issue, name='edit_issue'),
    url(r'^comment/new/$', create_or_edit_comment, name='new_comment'),
    url(r'^comment/(?P<pk>\d+)/edit/$', create_or_edit_comment, name='edit_comment'),
    url(r'^comment/(?P<pk>\d+)/del_cmt/$', del_comment, name='del_comment')
    ]