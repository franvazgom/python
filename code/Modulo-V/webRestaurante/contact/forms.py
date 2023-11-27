from django import forms
from django.core.exceptions import ValidationError

def valida_dominio(email):
    dominio = 'google.com'
    if dominio not in email:
        raise ValidationError(f'El correo electrónico debe ser: {dominio}')

class ContactForm(forms.Form):
    name            = forms.CharField(
        	            label       = 'Nombre',
                        required    = True,
                        widget      = forms.TextInput(
                            attrs   = {
                                'class'         : 'form-control',
                                'placeholder'   : 'Escribe tu nombre',
                            }
                        ),
                        min_length  = 3,
                        max_length  = 100,
                    )
    email           = forms.EmailField(
                        validators=[valida_dominio], 
                        label       = 'Email',
                        required    = True,
                        widget      = forms.EmailInput(
                            attrs   = {
                                'class'         : 'form-control',
                                'placeholder'   : 'Escribe tu email',
                            }
                        ),
                        min_length  = 3,
                        max_length  = 100,
                    )
    content         = forms.CharField(
                        label       = 'Contenido',
                        required    = True,
                        widget      = forms.Textarea(
                            attrs   = {
                                'class'         : 'form-control',
                                'placeholder'   : 'Escribe tu mensaje',
                                'rows'          : '4',
                            }
                        ),
                        min_length  = 3,
                        max_length  = 100,
                    )


class ContactForm2(forms.Form):
    name            = forms.CharField(min_length=5)
    email           = forms.EmailField(validators=[valida_dominio])
    content         = forms.CharField()