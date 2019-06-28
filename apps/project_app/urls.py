from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^log_in$', views.log_in),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^proj_board$', views.proj_board),
    url(r'^new_project$', views.new_project),
    url(r'^create_project$', views.create_project),
    url(r'^view_project/(?P<project_id>\d+)$', views.view_project),
]