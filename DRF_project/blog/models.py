from django.conf import settings
from django.db import models
from django.urls import reverse

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=1)
    title=      models.CharField(max_length=200)
    des=        models.CharField(max_length=300)

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk": self.id})
    