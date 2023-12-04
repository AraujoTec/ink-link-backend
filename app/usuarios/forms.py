from django import forms
from app.usuarios.models import Usuarios

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Usuarios
        fields = ('nome', 'email', 'password', 'data_cadastro', 'data_nascimento', 'ativo', 'funcao', 'cpf', 'empresa_id')
        