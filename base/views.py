from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.utils.translation import gettext_lazy as _
# Create your views here.
def updates(request):
    return render(request, 'updates.html')


def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})



def blog(request):
    return render(request, 'blog.html')

@login_required(login_url='login')
def deletepost(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('counter')
    return render(request, 'delete.html', {'post': post})


def languges(request):
    return render(request, 'languges.html')



def updatepost(request, post_id):

    post = Post.objects.get(id=post_id)
    if request.user != post.author:
        return redirect("/")
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid:
            form.save()
            return redirect('counter')
        
    return render(request, 'update-post.html', {'form': form})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request. POST[ 'password']
        password2 = request. POST[ 'password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'password do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request. POST[ 'password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('counter')

        else:
            messages.info(request, 'account is invalid!')
            return redirect('login')

    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')
def comment(request, post_id):

    form = CommentForm
    if request.method == 'POST':
        form = CommentForm(request=POST)
        if form.is_valid:
            form.save()
    return render(request, 'comment.html',{'form': form})



# myapp/views.py


def share_twitter_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        twitter_post_url = request.POST.get("twitter_post_url")
        Tweet.objects.create(title=title, twitter_post_url=twitter_post_url)
        return redirect("home")  # Redirect to the home page
    return render(request, "share_twitter_post.html")

def display_shared_tweets(request):
    shared_tweets = Tweet.objects.all()
    return render(request, "shared_tweets.html", {"shared_tweets": shared_tweets})



def CreatePost(request):
    form = PostForm
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('counter')
    return render(request, 'createpost.html',{'form': form})

@login_required(login_url='register')
def userslist(request):
    profiles = Profile.objects.exclude(user=request.user)
    context = {'profiles': profiles}
    return render(request, 'users.html', context)

def follow(request, user_id):
    profile = Profile.objects.get(user=request.user)
    follow = Profile.objects.get(id=user_id)
    profile.followings.add(follow)
    profile.save()
    return redirect('counter')

def profile(request, user_id):
    profile = User.objects.get(id=user_id)
    user_posts = profile.post_set.all()
    form = ProfileForm
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid:
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
    context = {'profile': profile, 'user_posts': user_posts, 'form': form}
    return render(request, 'profile.html', context)

def counter(request):
    query = request.GET.get("q", "")
    posts = Post.objects.filter(
        title__icontains=query
    )

    context = {
        'posts': posts,
    }
    return render(request, 'counter.html', context)



def twitter_posts(request):
    tweets = Twitter.objects.all()

    context = {
        'tweets': tweets,
    }
    return render(request, 'twitter.html', context)



def post(request, id):
    post = Post.objects.get(id=id)
    view, created = View.objects.get_or_create(post=post)
    view.views += 1
    view.save()
    
    form = CommentForm
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
    context = {'post': post, 'form': form, 'view': view}
    return render(request, 'post.html', context)

def like_post(request, post_id):
    if not request.user.is_authenticated:
        messages.info(request, 'account is not loged!')
        return redirect('counter')
    
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        if request.user not in post.likes.all():
            post.likes.add(request.user)
        else:
            post.likes.remove(request.user)
        post.save()
        return redirect('counter')
