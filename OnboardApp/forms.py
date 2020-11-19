from django import forms
from .models import Contacto,Lugar,Resena
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        # fields = ["nombre","correo","tipo_consulta","mensaje","avisos"]
        fields = '__all__'


class ResenaForm(forms.ModelForm):

    class Meta:
        model = Resena
        fields = '__all__'

class LugarForm(forms.ModelForm):

    imagen = forms.ImageField(required=False,validators=[MaxSizeFileValidator(max_file_size=2)])
    nombre = forms.CharField(min_length=3,max_length=50)
    precio = forms.IntegerField(min_value=1,max_value=2000000)

    # def clean_nombre(self):
    #     nombre = self.cleaned_data["nombre"]
    #     existe = Lugar.objects.filter(nombre__iexact=nombre).exists()

    #     if existe:
    #         raise ValidationError("Este nombre ya existe")
    #     return nombre

    class Meta:
        model = Lugar
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]