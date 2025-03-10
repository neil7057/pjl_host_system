from django import forms
from .models import Timeperiod


class TimeperiodForm(forms.ModelForm):

    class Meta:
        model = Timeperiod
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
