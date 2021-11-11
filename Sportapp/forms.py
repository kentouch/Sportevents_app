from django import forms

from Sportapp.models import Comment

# creating a form

class CommentForm(forms.ModelForm):
   class Meta:
       model = Comment
       fields = ('name', 'email', 'body')

       widgets ={
           'name': forms.TextInput(attrs={'class': 'form_control'}),
           'email': forms.TextInput(attrs={'class': 'form_control'}),
           'body':forms.Textarea(attrs={'class': 'form_control'}),
       }