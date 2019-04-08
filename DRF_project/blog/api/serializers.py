from rest_framework.serializers import (
    ModelSerializer, 
    HyperlinkedIdentityField,
    SerializerMethodField,
)

from .. import models

class PostCreateUpdateSerializer(ModelSerializer):
   class Meta:
       model = models.Post
       fields = [
           'title',
           'des',
       ]

class PostSerializer(ModelSerializer):

    user_name = SerializerMethodField()

    # you have to create get_absolute_url in models
    url = HyperlinkedIdentityField(
        read_only=True,
        view_name = 'blog:detail',
        lookup_field = 'pk'
        )

    class Meta:
       model = models.Post
       fields = [
           'url',
           'user',
           'id',
           'title',
           'des',
           'user_name',
       ]

    def get_user_name(self , obj):
        return str(obj.user.username)

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
