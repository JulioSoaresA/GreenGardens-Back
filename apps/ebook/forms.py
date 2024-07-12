from django import forms
from .models import CadastroEbook
from django.core.exceptions import ValidationError


class CadastroEbookForm(forms.ModelForm):
    class Meta:
        model = CadastroEbook
        fields = ['nome', 'email', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CadastroEbook.objects.filter(email=email).exists():
            raise ValidationError("Este e-mail já está registrado.")
        return email

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if CadastroEbook.objects.filter(telefone=telefone).exists():
            raise ValidationError("Este telefone já está registrado.")
        return telefone
