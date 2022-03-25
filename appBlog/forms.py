from dataclasses import field, fields
from django import forms
from appBlog.models import Blog, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=('comment_text',)
