from django.forms import ModelForm
from .models import Usuari

class PersonForm(ModelForm):
    class Meta:
        model = Usuari
        fields = '__all__'