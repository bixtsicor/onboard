from django import forms
from .models import Contacto,Lugar

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        # fields = ["nombre","correo","tipo_consulta","mensaje","avisos"]
        fields = '__all__'

class LugarForm(forms.ModelForm):
    class Meta:
        model = Lugar
        fields = '__all__'