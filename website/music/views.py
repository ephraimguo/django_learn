# from django.http import Http404
# from django.http import HttpResponse
from .models import Album, Song
# from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404

def index(request):
    all_albums = Album.objects.all() #connect to the database to get all the albums as objects!!
    # html = ''
    # for album in all_albums:
    #     url = '/music/'+str(album.id) + '/'
    #     html += '<a href="#">'+album.album_title +'</a><br>'


    # this command will directly picking up the file in the app/template folder, the template folder name is pl. form

    # template = loader.get_template('music/index.html')
    return render(request, 'music/index.html', {'all_albums': all_albums,})

def detail(request, album_id):
    # return HttpResponse('<h2>Detail of the album id %s </h2>' %str(album_id))
    # try :
    #     album = Album.objects.get(pk = album_id)
    # except Album.DoesNotExist:
    #     raise Http404('Album does not exist')

    #shortcut for above content
    album = get_object_or_404(Album, pk=album_id)
    return render(request,  'music/detail.html', {'album': album}, )

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {'album': album, 'error_message':'You did not select a valid song',})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})