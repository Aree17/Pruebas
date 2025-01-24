from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from formulas.forms import CustomAuthenticationForm  # Ya lo tienes
from .forms import CustomUserCreationForm  # Importamos el formulario personalizado

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomAuthenticationForm  # El formulario personalizado para el login

class CustomRegisterView(FormView):  # Cambiamos a FormView para manejar el formulario de registro
    template_name = 'register.html'
    form_class = CustomUserCreationForm  # Usamos el formulario personalizado
    success_url = reverse_lazy('login')  # Redirige al login tras un registro exitoso

    def form_valid(self, form):
        form.save()  # Guarda el nuevo usuario
        return super().form_valid(form)
