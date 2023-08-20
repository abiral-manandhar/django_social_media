import json

from django.shortcuts import render, get_object_or_404
from django.forms import formset_factory
from .forms import ImageForm, PostForm
from .models import Post, Image
from django.views.generic import ListView, RedirectView, DetailView
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .forms import CommentForm
from django.views.generic  import View
from .models import Comment, Post
from django.core import serializers
from django.views.generic.edit import FormMixin

class LikeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        print(pk)
        obj = get_object_or_404(Post,  pk=pk)
        user=self.request.user
        url_ = obj.get_absolute_url()

        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_



class ListUsers(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk=None, format=None):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(Post, pk=pk)
        user = self.request.user
        url_ = obj.get_absolute_url()
        updated = False
        liked=False

        if user.is_authenticated:
            if user in obj.likes.all():
                liked=False
                obj.likes.remove(user)
            else:
                liked=True
                obj.likes.add(user)
            updated=True
        data = {
            'updated': updated,
            'liked': liked,
        }
        return Response(data)

def add_post(request):
    if request.method == "POST":

        data = request.POST
        images = request.FILES.getlist(
            'images'
        )

        post = Post.objects.create(description = data.get('description'), user = request.user)
        for f in images:
            photo = Image.objects.create(
                post = post,
                image =f
            )

    return render(request, 'post/add.html')


class PostListView(ListView):
    template_name = 'post/list.html'
    model = Post
    form_class=CommentForm
    context_object_name = 'posts'
def PostListView(request):
    context = {

        'form': CommentForm(),
        'posts': Post.objects.all(),
    }

    print()

    if request.method =="POST":

        print(request.POST)
        form = CommentForm(request.POST)

        if form.is_valid():
            print('VALID')


    return render(request, 'post/list.html', context)

class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'p'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(Comment, self).form_valid(form)


from django.http import JsonResponse

class PostJsonListView(View):
    def get(self, *args, **kwargs):

        size = False
        print(kwargs)
        upper = kwargs.get('num_posts')
        pk = kwargs.get('pk')
        print("-----------", pk)
        lower = upper - 1
        print(lower, upper)
        post = Post.objects.get(pk=pk)

        cl = Comment.objects.filter(post=post)
        comments = serializers.serialize('json', cl[lower:upper])
        print(comments)
        commenters = []
        urls = []
        for i in Comment.objects.filter(post=post):
            commenters.append(i.commenter.username)

        for i in Comment.objects.filter(post=post):
            urls.append(i.commenter.profile.profile_pic.url)

        comments_size = len(json.loads(serializers.serialize('json',Comment.objects.filter(post=post))))
        print(comments_size)

        size=True if upper>=comments_size else False
        print("-----xxxxxxxxxxxxxxxx----------", comments, size)

        return JsonResponse({'data':  comments, 'max': size,'urls': urls,'commenters': commenters}, safe=False)