from django.conf.urls import url

from . import views

app_name = 'presskit'
urlpatterns = [
    url(r'^$', views.presskit, name='default'),
    url(r'^(?P<company_slug>[-\w]+)/$', views.presskit, name='company'),
    url(r'^projects/(?P<project_slug>[-\w]+)/$', views.project, name='project'),
    url(r'^projects/(?P<project_slug>[-\w]+)/data.xml$', views.project_xml, name='project_xml'),
    url(r'^projects/(?P<project_slug>[-\w]+)/images/header.png$', views.project_header, name='project_header'),
]
