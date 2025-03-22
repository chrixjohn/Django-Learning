from django.forms import ModelForm
from .models import movieinfo

class movieform(ModelForm):
    class Meta:
        model=movieinfo
        fields='__all__'