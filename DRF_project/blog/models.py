from django.db import models

class Post(models.Model):
    title=      models.CharField(max_length=200)
    des=        models.CharField(max_length=300)

