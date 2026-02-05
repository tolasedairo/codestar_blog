from django import forms
from .models import Comment  # Only Comment, not CollaborateRequest

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
