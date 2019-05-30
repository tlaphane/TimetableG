from django.conf.urls import include,url
from . import views


urlpatterns = [

    url(r'^$', views.logg),
    url(r'^logged', views.logg),


]

