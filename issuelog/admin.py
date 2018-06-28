from django.contrib import admin
from .models import Issue, Comment

# Register your models here.

# admin.site.register(Issue)
# admin.site.register(Comment)


class CommentAdmin(admin.TabularInline):
    model = Comment
    
class IssueAdmin(admin.ModelAdmin):
    inlines = (CommentAdmin, )
    
admin.site.register(Issue, IssueAdmin)