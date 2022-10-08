from dataclasses import field
from xml.etree.ElementTree import Comment
from django.forms import ModelForm
from posts.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]
