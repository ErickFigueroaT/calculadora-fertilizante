from django import forms
from .models import TipoCultivo, Cultivo

class FormTipoCultivo(forms.ModelForm):

    class Meta:
        model = TipoCultivo
        fields = '__all__'

class FormCultivo(forms.ModelForm):

    class Meta:
        model = Cultivo
        fields = '__all__'