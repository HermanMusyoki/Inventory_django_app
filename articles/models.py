from django.db import models

class ArticleManager(models.manager):
    def search(self, query):
        return Article.objects.filter(title__icontains = query)

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamb = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)

    objects = ArticleManager()

