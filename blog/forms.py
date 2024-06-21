from django import forms
from .models import Post

class Ni(forms.Form):

        nome = forms.CharField(label="Nome", max_length=100)
        cognome = forms.CharField(label="Cognome", max_length=100)
        telefono = forms.IntegerField(label="Telefono")
        email = forms.EmailField(label="Email", max_length=100)
        
        

class PostForm(forms.ModelForm):

        class Meta:
            model = Post
            fields = ('title', 'text',)









    
