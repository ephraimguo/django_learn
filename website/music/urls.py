from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/  which is the music home page
    re_path(r'^$', views.index, name='index'),

    # /music/[id] which is the details pages for specific album
    re_path(r'^(?P<album_id>\d+)/$', views.detail, name='detail'),

    #/music/[id]/favorite the favorite page
    re_path(r'^(?P<album_id>\d+)/favorite$', views.favorite, name='favorite'),

]