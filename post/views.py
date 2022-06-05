
from django.http.response import Http404
from post.models import Post, Comment, Profile, Like, Follow
from django.shortcuts import redirect, render
from .forms import CreateUserForm, UploadImageForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
import json
from django.contrib.auth.models import User



def comment(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment_form.instance.user = request.user.profile
            comment_form.instance.post = post

            comment_form.save()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
def like(request, post_id):
    user = request.user
    post = Post.objects.get(pk=post_id)
    like = Like.objects.filter(user=user, post=post)
    if like:
        like.delete()
    else:
        new_like = Like(user=user, post=post)
        new_like.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def follow(request, user_id):
    user = request.user
    other_user = User.objects.get(pk=user_id)
    follow = Follow.objects.filter(follower=user, followed=other_user)
    if follow:
        follow.delete()
    else:
        new_follow = Follow(follower=user, followed=other_user)
        new_follow.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
