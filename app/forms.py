from django import forms


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