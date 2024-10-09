from django import forms
from .validators import validate_pesel

class PeselNumberForm(forms.Form):
    pesel = forms.CharField(label='Numer PESEL', max_length=11, validators=[validate_pesel])