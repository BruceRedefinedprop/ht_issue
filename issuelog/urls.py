from django.conf.urls import url
from .views import get_posts, post_detail, create_or_edit_post, create_or_edit_comment, del_comment

urlpatterns = [
    url(r'^$', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_or_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post'),
    url(r'^comment/new/$', create_or_edit_comment, name='new_comment'),
    url(r'^comment/(?P<pk>\d+)/edit/$', create_or_edit_comment, name='edit_comment'),
    url(r'^comment/(?P<pk>\d+)/del_cmt/$', del_comment, name='del_comment')
    ]