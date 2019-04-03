from rest_framework.serializers import ModelSerializer
from .. import models

class PostSerializer(ModelSerializer):
   class Meta:
       model = models.Post
       fields = [
           'id',
           'title',
           'des',
       ]
