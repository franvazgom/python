from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.urls import reverse_lazy
from .forms import UserCreationFormWithEmail

class SignUpView(CreateView): 
    # form_class = UserCreationForm
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self): 
        return reverse_lazy('login') + '?register'
    
    def get_form(self, form_class=None): 
        form = super(SignUpView, self).get_form()
        #Se realizan los cambios al formulario        
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2'})
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2'})
        return form


