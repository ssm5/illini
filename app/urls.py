from django.conf.urls import url

from . import views

app = "app"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<organization_id>[0-9]+)/$', views.detail, name='detail'),
]
