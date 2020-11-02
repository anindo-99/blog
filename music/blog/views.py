from django.shortcuts import render, redirect
from .models import Post ,Blogcomment
from django.contrib import messages
from blog.templatetags import extras
from itertools import chain
from django.contrib.sessions.models import Session

# Create your views here.


def bloghome(request):
    # allPosts = Post.objects.all()
    allPosts = Post.objects.all()
    # allPost2 = Blogupload.objects.all()
    # allPosts = list(chain(allPost1, allPost2))

    context = {'allPosts':allPosts}
    return render(request, 'blog/bloghome.html', context)


def blogPost(request,slug):

    post = Post.objects.filter(slug=slug).first()
    post.views = post.views+1
    post.save()
    # post_from_user = Blogupload.objects.filter(slug=slug).first()
    # # post_from_user.bviews = post_from_user.bviews+1
    # # post_from_user.save()
    
   
    comments = Blogcomment.objects.filter(post=post,parent=None)
    replies = Blogcomment.objects.filter(post=post).exclude(parent=None)
    repDict = {}
    for reply in replies:
        if reply.parent.sno not in repDict.keys():
            repDict[reply.parent.sno] = [reply]
        else:
            repDict[reply.parent.sno].append(reply)
    context = {'post':post,'comments':comments,'repDict':repDict}
    return render(request, 'blog/blogPost.html',context)


def postComment(request):

    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")

        if parentSno=="":

            comments = Blogcomment(comment=comment,user=user,post=post)
            comments.save()

            messages.success(request,"Your comment has been posted successfully")
        else:
            parent = Blogcomment.objects.get(sno=parentSno)
            comments = Blogcomment(comment=comment, user=user, post=post,parent=parent)
            comments.save()

            messages.success(request,"Your reply has been posted successfully")
    return redirect(f"/blog/{post.slug}")



def blogupload(request):
    if request.session.has_key('is_logged'):
        return render(request, 'blog/blogupload.html')
    return redirect('bloghome')

def bloguploaded(request):

    if request.method== 'POST':
        btitle = request.POST.get('btitle')
        bauthor = request.POST.get('bauther')
        bimages = request.POST.get('bimages')
        bcontent = request.POST.get('bcontent')
        bviews = 0
        

        blog_uploads = Post(title=btitle, author=bauthor, slug=btitle,content=bcontent,views=bviews,timestamp="")
        blog_uploads.save()

        print(blog_uploads)

        messages.success(request, "Your blog has been uploaded successfully")

    return redirect('bloghome')

    # return render(request, 'blog/blogupload.html')


# def blogPostUpload(request, bslug):

#     post = Blogupload.objects.filter(bslug=bslug).first()
#     post.views = post.views+1
#     post.save()
#     print(post)
#     # post_from_user = Blogupload.objects.filter(slug=slug).first()
#     # # post_from_user.bviews = post_from_user.bviews+1
#     # # post_from_user.save()

#     comments = Blogcomment.objects.filter(post=post, parent=None)
#     replies = Blogcomment.objects.filter(post=post).exclude(parent=None)
#     repDict = {}
#     for reply in replies:
#         if reply.parent.sno not in repDict.keys():
#             repDict[reply.parent.sno] = [reply]
#         else:
#             repDict[reply.parent.sno].append(reply)
#     context = {'post': post, 'comments': comments, 'repDict': repDict}
#     print(context)
#     return render(request, 'blog/blogPostUpload.html', context)
