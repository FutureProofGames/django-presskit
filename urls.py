from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.presskit, name='default'),
    url(r'^(?P<company_slug>[-\w]+)/$', views.presskit, name='company'),
    url(r'^(?P<company_slug>[-\w]+)/images.zip$', views.company_zip, name='company_zip'),
    url(r'^(?P<company_slug>[-\w]+)/logos.zip$', views.company_logo_zip, name='company_logo_zip'),
    url(r'^projects/(?P<project_slug>[-\w]+)/$', views.project, name='project'),
    url(r'^projects/(?P<project_slug>[-\w]+)/data.xml$', views.project_xml, name='project_xml'),
    url(r'^projects/(?P<project_slug>[-\w]+)/images/header.png$', views.project_header, name='project_header'),
    url(r'^projects/(?P<project_slug>[-\w]+)/images.zip$', views.project_zip, name='project_zip'),
    url(r'^projects/(?P<project_slug>[-\w]+)/logos.zip$', views.project_logo_zip, name='project_logo_zip'),
]
