from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Comments,Post

class PostForm(forms.ModelForm):

    class Meta:
        model  = Post
        fields = ('author','title','text')
        widgets ={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.TextInput(attrs={'class':"editable medium-editor-textarea postcontent"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model =Comments
        fields = ('author','text')

        widgets={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.TextInput(attrs={'class':"editable medium-editor-textarea"}),
        }