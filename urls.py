from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.presskit, name='default'),
    url(r'^(?P<company_id>[0-9]+)/$', views.presskit, name='company'),
    url(r'^(?P<company_id>[0-9]+)/images.zip$', views.company_zip, name='company_zip'),
    url(r'^(?P<company_id>[0-9]+)/logos.zip$', views.company_logo_zip, name='company_logo_zip'),
    url(r'^projects/(?P<project_id>[0-9]+)/$', views.project, name='project'),
    url(r'^projects/(?P<project_id>[0-9]+)/images.zip$', views.project_zip, name='project_zip'),
    url(r'^projects/(?P<project_id>[0-9]+)/logos.zip$', views.project_logo_zip, name='project_logo_zip'),
]
