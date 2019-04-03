from django.http import HttpResponse
from rest_framework.generics import (
   ListAPIView, 
   RetrieveAPIView,
   UpdateAPIView,
   DestroyAPIView,
   CreateAPIView
)
from rest_framework.filters import (
   SearchFilter,
   OrderingFilter
)
from blog import models
from .serializers import PostSerializer, PostDetailSerializer, PostCreateUpdateSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwnerOrReadOnly

class PostListAPIView(ListAPIView):
   queryset = models.Post.objects.all()
   serializer_class = PostSerializer

   filter_backends = [SearchFilter]
   search_fields = ['title', 'des']
   #http://127.0.0.1:8000/api/posts/?search=masht&ordering=title    -reverse order

class PostDetailAPIView(RetrieveAPIView):
   queryset = models.Post.objects.all()
   serializer_class = PostDetailSerializer


class PostUpdateAPIView(UpdateAPIView):
   queryset = models.Post.objects.all()
   serializer_class = PostCreateUpdateSerializer
   permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]

   def perform_update(self , serializer):
      serializer.save(user=self.request.user)

class PostDeleteAPIView(DestroyAPIView):
   queryset = models.Post.objects.all()
   serializer_class = PostDetailSerializer


class PostCreateAPIView(CreateAPIView):
   queryset = models.Post.objects.all()
   serializer_class = PostCreateUpdateSerializer
   permission_classes = [IsAuthenticated ,IsAdminUser]

   def perform_create(self, serializer):
      serializer.save(user=self.request.user)