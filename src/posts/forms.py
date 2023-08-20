from django.forms import ModelForm
from .models import Post, Image, Comment
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['description',]

class ImageForm(ModelForm):
    image = forms.FileField(widget = forms.ClearableFileInput(attrs = {'multiple': True, 'name': 'images'}))
    class Meta:
        model = Image
        fields = ['image',]

class CommentForm(ModelForm):

    comment = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-field', 'placeholder': 'Write a comment...'}))
    class Meta:
        model = Comment
        fields = ['comment','post']