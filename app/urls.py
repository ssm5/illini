from django.conf.urls import url

from . import views

app = "app"

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
