from django import forms
# from .widgets import CustomClearableFileInput
from .models import Organisation


class OrganisationForm(forms.ModelForm):

    class Meta:
        model = Organisation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-15'
            field.widget.attrs['aria-label'] = field_name
