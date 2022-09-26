from rest_framework import generics,permissions
from rest_framework.authentication import get_user_model
from rest_framework import viewsets
from posts.serializers import PostSerializer,UserSerializer
from.models import Post 
from .permissions import IsAuthorOrNot


class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    permission_classes = (IsAuthorOrNot,)
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=get_user_model().objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer



