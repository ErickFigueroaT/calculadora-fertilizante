from django import forms 
from django.contrib.auth.models import User

# Importaciones necesarias
# - forms: Módulo de formularios de Django
# - User: Modelo de usuario de Django

# Formulario para la creación de usuarios
class UserForm(forms.ModelForm):
    repassword = forms.CharField()
    email =forms.EmailField(required=True)
    class Meta:
        model = User  # Modelo asociado al formulario (User)
        fields = ('username','password','email','repassword')  # Campos del modelo que se incluirán en el formulario


    def clean_password(self,*args, **kwargs):
        if self.data['password'] and self.data['password'] != self.data['repassword']:
            raise forms.ValidationError('Las contraseñas son diferente; favor de verificar')
        return self.data['password']
    
    # Método para guardar el formulario
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)  # Guarda el usuario sin guardarlo en la base de datos aún
        user.set_password(self.cleaned_data['password'])  # Establece la contraseña del usuario
        if commit:
            user.save()  # Guarda el usuario en la base de datos si commit es True
        return user  # Devuelve el usuario guardado
 