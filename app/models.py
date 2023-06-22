from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    groups = models.ManyToManyField('auth.Group', blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField('auth.Permission', blank=True, related_name='custom_user_set')

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    creation_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
