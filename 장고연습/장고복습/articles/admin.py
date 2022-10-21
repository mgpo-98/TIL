from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'create_at', 'update_at']

admin.site.register(Article, ArticleAdmin)
