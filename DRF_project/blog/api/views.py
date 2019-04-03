from django.http import HttpResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView
from blog import models
from .serializers import PostSerializer


class PostListAPIView(ListAPIView):
   queryset = models.Post.objects.all()
   serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer



