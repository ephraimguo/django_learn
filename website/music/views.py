from django.http import HttpResponse
from .models import Album
# from django.template import loader
from django.shortcuts import render

def index(request):
    all_albums = Album.objects.all() #connect to the database to get all the albums as objects!!
    # html = ''
    # for album in all_albums:
    #     url = '/music/'+str(album.id) + '/'
    #     html += '<a href="#">'+album.album_title +'</a><br>'


    # this command will directly picking up the file in the app/template folder, the template folder name is pl. form

    # template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', )

def detail(request, album_id):
    return HttpResponse('<h2>Detail of the album id %s </h2>' %str(album_id))
