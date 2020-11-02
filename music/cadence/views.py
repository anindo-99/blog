from django.shortcuts import render,redirect
from cadence.models import Contact, Suserupload, Userprofile
from blog.models import Post
from songs.models import Songpost
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# from .forms import CreateUserForm
# Create your views here.
def index(request):
    supload = []
    postss = Post.objects.filter().order_by('-views')[:3]
    musics = Songpost.objects.filter().order_by('-plays')[:3]
    
    suploads = Suserupload.objects.all()
    n = len(suploads)
    supload.append([suploads,range(1,n)])
    
    context = {'postss': postss, 'musics':musics,'supload': supload}
    
    return render(request,'cadence/index.html',context)


@login_required(login_url='index')

def contact(request):
    

    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']
        content = request.POST['content']

        if len(first_name) < 2 or len(first_name) < 2 or len(last_name) < 2 or len(email) < 4 or len(phone) < 7 or len(city) < 2 or len(state) < 3 or len(zip_code) < 6 or len(content)<4:
            messages.error(request,"Please fill up the form correctly!")
        
        else:

            contact = Contact(first_name=first_name,last_name=last_name,email=email,phone=phone,city=city,state=state,zip_code=zip_code,content=content)
            contact.save()
            messages.success(request,"Your message has been successfully sent.")
    return render(request, 'cadence/contact.html')



def about(request):
    return render(request, 'cadence/about.html')




def upload(request):
    if request.session.has_key('is_logged'):
        return render(request, 'cadence/upload.html')
    else:
        
        return redirect('songhome')

def search(request):
    query = request.GET['search']

    if len(query)>78 or len(query)<1:
        allPosts = Post.objects.none()
        messages.error(request,"invalid query")

    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count()==0:
        messages.warning(request, "OOPS! No result found.")
    params  = {'allPosts':allPosts,'query':query}
    return render(request,'cadence/search.html',params)

#Authentication APIs
def handleSignup(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        if len(username)>10:
            messages.error(request,"username should be less than 10 characters")
            return redirect("index")

        if not username.isalnum():

            messages.error(request, "username should be alphanumeric")
            return redirect("index")
        for c in username:
            if c.isupper():

                messages.error(request, "username should be in lower case")
                return redirect("index")
                break
            
        if pass1 != pass2:
            messages.error(request, "Passwords dit not match")
            return redirect("index")

        
            

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        # Userprofile.objects.get(user=request.user,)

        messages.success(request,"Your Cadence account has been created successfully.")
        return redirect("index")
    else:
        return HttpResponse("404 - Not Found")

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['lusername']
        loginpassword = request.POST['pass']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request,"Succesfully logged in")
            request.session['is_logged'] = True

            return redirect("index")
        else:
            messages.error(request, "Invalid credentials, Please try again")
            return redirect("index")
    else:
        return HttpResponse("404 - Not Found")


def profile(request):
    # if request.method == 'POST':
    #     user = request.user
    #     profile_pic = request.POST.get("")
    #     phone = request.POST.get("")
    #     city = request.POST.get("")
    #     state = request.POST.get("")
    #     zip_code = request.POST.get("")

    #     user_profile = Userprofile(user=user,profile_pic=profile_pic,phone=phone,city=city,state=state,zip_code=zip_code)
    user_profile = Userprofile.objects.get(user__id=request.user.id)

    context = {'user_profile': user_profile}
    
    
        
    return render(request,'cadence/profile.html',context)


def editprofile(request):
    if request.session.has_key('is_logged'):
        user_profile = Userprofile.objects.get(user__id=request.user.id)

        context = {'user_profile': user_profile}

        # if 

        return render(request, 'cadence/editprofile.html', context)
    else:

        return redirect('index')


def handleEditProfile(request):
    user_profile = Userprofile.objects.get(user__id=request.user.id)
    if request.method=='POST':
        
        
        
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        phone = request.POST["phone"]

        usr = User.objects.get(id=request.user.id)

        usr.first_name = first_name
        usr.last_name = last_name
        usr.email = email
        usr.save()

        user_profile.phone = phone
        if len(phone)!=10:
            messages.error(request, "Invalid Phone number")
            return redirect('editprofile')
        else:
            user_profile.save()
            if "bimages" in request.FILES:
                profile_pic = request.FILES["bimages"]
                user_profile.profile_pic = profile_pic
                user_profile.save()

        messages.success(request,"You profile has been edited successfully")
        return redirect('profile')


def handleLogout(request):
    # del request.session['is_logged']
    logout(request)
    
    messages.success(request, "Succesfully logged out")
    return redirect("index")
