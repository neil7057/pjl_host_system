from django import forms
# from .widgets import CustomClearableFileInput
from .models import Host
from category.models import Category


class HostForm(forms.ModelForm):

    class Meta:
        model = Host
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-15'
            field.widget.attrs['aria-label'] = field_name
