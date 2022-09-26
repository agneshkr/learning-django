from rest_framework import generics,permissions

from posts.serializers import PostSerializer
from.models import Post 
from .permissions import IsAuthorOrNot

class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    permission_classes = (IsAuthorOrNot,)
    serializer_class=PostSerializer

class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    permission_classes = (IsAuthorOrNot,) #how to do this with function views
    serializer_class=PostSerializer

