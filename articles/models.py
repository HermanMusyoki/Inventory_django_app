from django.db import models
from django.db.models import Q

class ArticleManager(models.Manager):
    def search(self, query= None):
        if query is None or query == "":
            return self.get_queryset().none()
        lookups = Q(title__icontains = query) | Q(content__icontains = query)
        return Article.objects.filter(lookups)

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamb = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)

    objects = ArticleManager()

