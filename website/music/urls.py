from django.urls import path, re_path
from . import views

urlpatterns = [
    # /music/  which is the music home page
    re_path(r'^$', views.index, name='index'),

    # /music/[id] which is the details pages for specific album
    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='details')
]