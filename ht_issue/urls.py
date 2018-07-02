"""ht_issue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/

The ht_issue urls.py laysout the navigation for entire site.

The site only has one index.html file which is located in the home app.

"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from home import urls as urls_home
from accounts.views import index as admin_index
from products import urls as urls_products
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from issuelog import urls as urls_issuelog
from roadmap import urls as urls_roadmap
from home.views import index
from django.views import static
from .settings import MEDIA_ROOT
from django.views.generic import RedirectView
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^home/', include(urls_home)),
    url(r'^issue/', include(urls_issuelog)),
    url(r'^$', index, name="index"),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^search/', include(urls_search)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^roadmap/', include(urls_roadmap)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
]
