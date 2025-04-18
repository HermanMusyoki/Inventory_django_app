from django.contrib import admin

from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'timestamps', 'updated', ]
    search_fields = ['title', 'content']
    raw_id_fields = ['user']


