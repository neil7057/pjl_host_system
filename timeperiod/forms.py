from django import forms
from .models import Timeperiod

from django.forms.widgets import DateInput


class TimeperiodForm(forms.ModelForm):

    class Meta:
        model = Timeperiod
        fields = '__all__'
        widgets = {
            'date_from': DateInput(attrs={'type': 'date'}),
            'date_to': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
