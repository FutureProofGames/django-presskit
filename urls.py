from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.presskit, name='default'),
    url(r'^(?P<company_slug>[0-9]+)/$', views.presskit, name='company'),
    url(r'^projects/(?P<project_slug>[0-9]+)/$', views.project, name='project'),
]
