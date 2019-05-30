from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.logg),

    url(r'^logged', views.logg),
]

