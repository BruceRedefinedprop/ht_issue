from django.conf.urls import url, include
from .views import roadmap

urlpatterns = [
    url(r'^$', roadmap, name='roadmap'),
    ]