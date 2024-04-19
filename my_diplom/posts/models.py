from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    likes_count = GenericRelation(Like)

    def __str__(self):
        return self.user

    @property
    def total_likes(self, instance):
        return instance.likes_count.count()

    objects = models.Manager()


# для доп. задания
# class PostImage(models.Model):
#     ...


class Comment(models.Model):
    author = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.author

    objects = models.Manager()
