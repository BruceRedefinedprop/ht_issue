from django.contrib import admin
from .models import Issue, Comment

# Register your models here.
"""
Set's up comment and issue will appear in the admin panel.
For each issue will have comments in-lines.
"""



# admin.site.register(Issue)
# admin.site.register(Comment)


class CommentAdmin(admin.TabularInline):
    model = Comment
    
class IssueAdmin(admin.ModelAdmin):
    inlines = (CommentAdmin, )
    
# puts comments inline under issues.
admin.site.register(Issue, IssueAdmin)