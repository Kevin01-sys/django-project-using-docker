from django import forms
from .models import Post

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Nombre',
    )

    email = forms.EmailField(
        label='Correo electrónico',
    )

    message = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea,
    )

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)