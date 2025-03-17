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

    # either child or adult record present
    # child must have age, age must be balnk if adult
    def clean(self):
        cleaned_data = super().clean()
        is_adult = cleaned_data.get("is_adult")
        is_child = cleaned_data.get("is_child")
        child_age = cleaned_data.get("child_age")

        if is_adult and is_child:
            msg = "Either Member is child or adult, can't be both"
            self.add_error("is_adult", msg)
            self.add_error("is_child", msg)

        if not is_adult and not is_child:
            msg = "Either Member is child or adult, Select one"
            self.add_error("is_adult", msg)
            self.add_error("is_child", msg)

        if is_child and (child_age is None or child_age == 0):
            msg = "Child age must be greater than 0"
            self.add_error("child_age", msg)

        if is_adult and child_age:
            msg = "No Child age required for Adult"
            self.add_error("child_age", msg)

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
