from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='defaultThumb.png',blank=True)
    author = models.ForeignKey(User,models.CASCADE,default=None)
    tags = TaggableManager()
    def __str__(self):
        return self.title

    def snippet(self):
        if len(self.body) > 50:
            return self.body[:50] + '...'
        else:
            return self.body

#python3.6 manage.py makemigrations
#python3.6 manage.py migrate
