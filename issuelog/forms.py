from django import forms
from .models import Post, Comment

class IssuePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =  fields = ('published_date', 'title', 'content', 'image', 'tag')
        widgets = {'published_date': forms.DateInput(attrs={'id': 'datetimepicker1'})}

class IssueCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('post', 'comment', 'rating')
  