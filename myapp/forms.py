from django import forms
from .models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('name','phone','email','body')
        widgets={
            'summary': forms.Textarea(attrs={'rows':2,'cols':4})
        }
        