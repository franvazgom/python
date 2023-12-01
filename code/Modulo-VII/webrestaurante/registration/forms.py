from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationFormWithEmail(UserCreationForm): 
    email = forms.EmailField(required=True, help_text="Email requerido")

    class Meta: 
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self): 
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya se encuentra registrado")
        return email