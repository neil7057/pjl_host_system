from django import forms
from .models import Members
import datetime
from django.core.exceptions import ValidationError

from django.forms.widgets import DateInput


class MembersForm(forms.ModelForm):

    class Meta:
        model = Members
        fields = '__all__'
        widgets = {
            'dbs_date': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-15'
            field.widget.attrs['aria-label'] = field_name

    # check if dbs date greater than today
    # blank dbs is allowed
    def clean_dbs_date(self):
        data = self.cleaned_data['dbs_date']
        if not data:
            return data
        else:
            if data < datetime.date.today():
                raise ValidationError(
                    "DBS Expiry Date must be later than today")
            return data
