from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import Post, Comment


class IssuePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =   ( 'title', 'published_date','content', 'image', 'tag' )
        widgets = {'published_date' : DatePickerInput() }

class IssueCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('post', 'comment')
  