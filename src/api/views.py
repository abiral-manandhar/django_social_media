from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer
from posts.models import Post, Comment

@api_view(['GET'])

def apiOverView(request):
    api_urls = {
        'add': '/add',
        'create': '/create'

    }

@api_view(['POST'])

def AddPost(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def CreateComment(request, pk):

    serializer = CommentSerializer(data=request.data)


    if serializer.is_valid():

        print(request.user)
        post=Post.objects.get(pk=pk)
        comment = Comment.objects.create(post=post, commenter=request.user, comment = request.data.get('comment'))

    return Response(serializer.data)


