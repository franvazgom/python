from django.forms import ModelForm, TextInput, Textarea
from services.models import Service

class ServiceForm(ModelForm):
    class Meta:
        model   = Service
        fields  = ['title', 'subtitle', 'content', 'image']
        widgets = {
            'title':TextInput(
                attrs={'class':'form-control', 'placeholder':'Títutlo'}),
            'subtitle':TextInput(
                attrs={'class':'form-control', 'placeholder':'Subtítutlo'}),
        }
    def clean(self):
        super(ServiceForm, self).clean()
        title = self.cleaned_data.get('title')
        if len (title) < 5:
            self.errors['title'] = self.error_class(['Mínimo 5 caractéres'])
        return self.cleaned_data
    
    