from django import forms
from django.forms import fields
from .models import Post
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    body=forms.CharField(widget=CKEditorWidget(),label="Text Editor")
    class Meta:
        model=Post
        fields=('body',)