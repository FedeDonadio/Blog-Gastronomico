import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VinoFormulario(forms.Form):
    varietal = forms.CharField()
    origen = forms.CharField()
    fecha = forms.DateField()
    temperatura = forms.IntegerField()

class PlatosFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=30)
    fecha = forms.DateField()
    cocinero = forms.CharField(max_length=40)
    receta = forms.CharField()

class PostresFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=40)
    fecha = forms.DateField()
    pastelero = forms.CharField(max_length=40)

class CafeFormulario(forms.Form):
    variedad = forms.CharField(max_length=40)
    filtrado = forms.CharField(max_length=40)
    barista = forms.CharField(max_length=40)
    origen = forms.CharField(max_length=40)

class QuesosFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    tipo = forms.CharField(max_length=40)
    origen = forms.CharField(max_length=40)
    pasteurizado = forms.BooleanField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields} 