from django.conf.urls import url, include
from . import urls_reset
from .views import index, register, profile, logout, login
"""
urls for registration, login and logout and password reset.
profile code exists as a test to see which user is logged in, butt
it is not wired into the navigation of the site.
"""
urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
]
