from django.contrib import admin
from .models import Post, Comment

# Register your models here.

# admin.site.register(Post)
# admin.site.register(Comment)


class CommentAdmin(admin.TabularInline):
    model = Comment
    
class PostAdmin(admin.ModelAdmin):
    inlines = (CommentAdmin, )
    
admin.site.register(Post, PostAdmin)