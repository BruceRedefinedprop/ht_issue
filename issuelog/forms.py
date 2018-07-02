from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import Issue, Comment

"""
configure forms for editing or creating issues and comments.
Datapicker is django addon for using calender to add a date to a field.

"""
class IssuePostForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields =   ( 'title','ht_product','published_date','content', 'image', 'tag' )
        widgets = {'published_date' : DatePickerInput() }

class IssueCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('issue', 'comment')
  