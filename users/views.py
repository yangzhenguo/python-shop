from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from models import *
from hashlib import sha1

# Create your views here.


def register(request):
    return render(request, 'users/register.html')


def register_handle(request):
    post = request.POST
    username = post.username
    password = post.password
    password2 = post.password2
    email = post.email
    if password != password2:
        return redirect('/users/register', 'a', 'b')
    password_sha = sha1(password).hexdigest()
    user = UserInfo(username=username, password=password_sha, email=email)
    return JsonResponse({'user', user})