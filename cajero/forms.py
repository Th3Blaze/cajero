from django import forms 
from . import models
from django.core.validators import MinValueValidator, MaxValueValidator

class LoginForm(forms.Form):
    usuario=forms.CharField()
    contrasena=forms.CharField()
    labels = {
            "usuario": "Usuario",  # Customizar el Label para el campo usuario
            "contrasena": "Contraseña",  # Customizar el Label para el campo contrasenha
        }


class GiroForm(forms.Form):
    cantidad=forms.DecimalField(max_digits=10,decimal_places=2)
    validators=[
            MinValueValidator(0.01, message="El valor debe ser mayor que 0"),
            MaxValueValidator(999999.99, message="El valor debe ser menor que 999999.99")
        ]
    

class DepositoForm(forms.Form):
    Cantidad=forms.DecimalField(max_digits=10,decimal_places=2)
    validators=[
            MinValueValidator(0.01, message="El valor debe ser mayor que 0"),
            MaxValueValidator(999999.99, message="El valor debe ser menor que 999999.99")
        ]
    

