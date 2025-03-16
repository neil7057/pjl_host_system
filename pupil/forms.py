from django import forms
from .models import Pupil

from django.forms.widgets import DateInput


class PupilForm(forms.ModelForm):

    class Meta:
        model = Pupil
        fields = '__all__'
        widgets = {
            'dob': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-15'
            field.widget.attrs['aria-label'] = field_name
