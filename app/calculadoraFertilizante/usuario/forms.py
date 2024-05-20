from django import forms
from django.contrib.auth.models import User

# Importaciones necesarias
# - forms: Módulo de formularios de Django
# - User: Modelo de usuario de Django

# Formulario para la creación de usuarios
class UserForm(forms.ModelForm):
    class Meta:
        model = User  # Modelo asociado al formulario (User)
        fields = ('username', 'password', 'email')  # Campos del modelo que se incluirán en el formulario

    # Método para guardar el formulario
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)  # Guarda el usuario sin guardarlo en la base de datos aún
        user.set_password(self.cleaned_data['password'])  # Establece la contraseña del usuario
        if commit:
            user.save()  # Guarda el usuario en la base de datos si commit es True
        return user  # Devuelve el usuario guardado
 