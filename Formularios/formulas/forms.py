# cuentas/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, label='Full Name')  # Campo para el nombre completo
    email = forms.EmailField(required=True)  # Campo para el correo electrónico
    phone_number = forms.CharField(max_length=15, label='Phone Number', required=False)  # Campo para el número de teléfono

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'phone_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['full_name']  # Guardamos el nombre completo en el campo 'first_name'
        user.email = self.cleaned_data['email']  # Guardamos el email
        if commit:
            user.save()
        return user