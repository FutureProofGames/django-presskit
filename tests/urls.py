from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('django_presskit.urls', namespace='django_presskit')),
]
