from rest_framework.serializers import ModelSerializer
from .. import models

class PostCreateUpdateSerializer(ModelSerializer):
   class Meta:
       model = models.Post
       fields = [
           'title',
           'des',
       ]

class PostSerializer(ModelSerializer):
   class Meta:
       model = models.Post
       fields = [
           'user',
           'id',
           'title',
           'des',
       ]

class PostDetailSerializer(ModelSerializer):
   class Meta:
       model = models.Post
       fields = [
           'id',
           'title',
           'des',
       ]


"""

from blog.models import Post
from blog.api.serializers import PostSerializer

obj = Post.objects.get(id=2)

data = {
    "title" : "Yeahh buddy",
    "des"   : "New content",
}

new_item = PostSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)    

"""
