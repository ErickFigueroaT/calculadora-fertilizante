from django import forms
from .models import TipoCultivo, Cultivo

# Formulario para el modelo TipoCultivo
class FormTipoCultivo(forms.ModelForm):
    class Meta:
        model = TipoCultivo  # Especifica el modelo asociado al formulario
        fields = '__all__'  # Utiliza todos los campos del modelo

# Formulario para el modelo Cultivo
class FormCultivo(forms.ModelForm):
    class Meta:
        model = Cultivo  # Especifica el modelo asociado al formulario
        fields = '__all__'  # Utiliza todos los campos del modelo
