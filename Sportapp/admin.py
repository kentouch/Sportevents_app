from django.contrib import admin
from .models import Category, Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'status','created_on')
    list_filter = ['status']
    search_fields = ['title', 'content']
  
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
