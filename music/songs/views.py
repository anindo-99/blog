from django.shortcuts import render, redirect
from songs.models import Songpost
from django.contrib import messages
from itertools import chain
# Create your views here.


def songhome(request):
    allPosts = Songpost.objects.all()
  
    # allPosts = Songpost.objects.filter().order_by('-plays')[:3]
    
    context = {'allPosts': allPosts}
    return render(request, 'songs/songhome.html', context)





def songPost(request, slug):

     

    post = Songpost.objects.filter(slug=slug).first()
    post.plays = post.plays+1
    # post.views = post.views+1
    post.save()
    
   

    # comments = Blogcomment.objects.filter(post=post, parent=None)
    # replies = Blogcomment.objects.filter(post=post).exclude(parent=None)
    # repDict = {}
    # for reply in replies:
    #     if reply.parent.sno not in repDict.keys():
    #         repDict[reply.parent.sno] = [reply]
    #     else:
    #         repDict[reply.parent.sno].append(reply)
    context = {'post': post}
    return render(request, 'songs/songPost.html', context)






def songuserPost(request):

    if request.method == 'POST':
        # title = request.POST.get("stitle")
        title = request.POST["stitle"]
        artist = request.POST.get("sartist")
        genre = request.POST.get("genre")
        artwork = request.FILES['artwork']
        tag = request.POST.get("tag")
        desc = request.POST.get("sdesc")
        music = request.FILES['music']
        album_title = request.POST.get("astitle")

        user_post = Songpost(song_title=title, artist=artist, genre=genre, slug=title,album_logo=artwork, album_title=album_title, file=music, tags=tag, desc=desc)
        user_post.save()

        messages.success(request, "Your song has been uploaded successfully")

    return redirect('songhome')
