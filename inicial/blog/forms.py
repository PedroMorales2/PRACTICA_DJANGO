# forms.py
from django.forms import ModelForm, TextInput, Textarea, DateInput
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['date','user']
        
        bton = {
            'class' : "btn btn-outline-success",
            'onclick' : "document.getElementById('file-input').click(); return false;",
            'name' : "file",
            'placeholder' : "FOTO/VIDEO"
        }
        
        widgets = {
            'content': Textarea(attrs={
                'placeholder': 'Escriba el contenido aquí...',
                'class': 'form-control',
                'rows': 5
            }),
            
            'image' : TextInput(attrs=bton),
            
            'title' : TextInput(attrs={
                'placeholder': 'Título',
                'class': 'form-control'
            }),
        }
