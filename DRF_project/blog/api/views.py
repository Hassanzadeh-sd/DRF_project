from django.http import HttpResponse
from rest_framework.generics import (
   ListAPIView, 
   RetrieveAPIView,
   UpdateAPIView,
   DestroyAPIView,
   CreateAPIView
)

from blog import models
from .serializers import PostSerializer, PostDetailSerializer, PostCreateUpdateSerializer


class PostListAPIView(ListAPIView):
   queryset = models.Post.objects.all()
   serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView):
   queryset = models.Post.objects.all()
   serializer_class = PostDetailSerializer



class PostUpdateAPIView(UpdateAPIView):
   queryset = models.Post.objects.all()
   serializer_class = PostCreateUpdateSerializer

   def perform_update(self , serializer):
      serializer.save(user=self.request.user)

class PostDeleteAPIView(DestroyAPIView):
   queryset = models.Post.objects.all()
   serializer_class = PostDetailSerializer


class PostCreateAPIView(CreateAPIView):
   queryset = models.Post.objects.all()
   serializer_class = PostCreateUpdateSerializer

   def perform_create(self, serializer):
      serializer.save(user=self.request.user)