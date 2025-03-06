from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for Review Model - Add / Edit
    """

    class Meta:
        model = Review
        fields = ('title', 'content', 'rating',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["rating"].widget.attrs['min'] = 1
        self.fields["rating"].widget.attrs['max'] = 5
        self.fields["rating"].widget.attrs['step'] = .1

        # Sets placeholder values
        placeholders = {
            'title': 'Title',
            'content': 'Your Review',
            'rating': 1
        }

        # Sets autofocus on first input
        self.fields['title'].widget.attrs['autofocus'] = True

        # Sets aria-labels on inputs
        self.fields['title'].widget.attrs['aria-label'] = 'Review Title'
        self.fields['content'].widget.attrs['aria-label'] = 'Review Content'
        self.fields['rating'].widget.attrs[
            'aria-label'] = 'Rating: Choose a value between 1-5'

        for field in self.fields:
            # Sets placeholders on fields with * for required fields
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]

            # Sets placeholders on inputs
            self.fields[field].widget.attrs['placeholder'] = placeholder

            # Adds stylings classes to inputs
            self.fields[field].widget.attrs['class'] = (
                'form-review text-indent rounded-15')

            # Removes input labels
            self.fields[field].label = False

        # Hidden input field for rating score
        # Accessible to screen readers
        self.fields['rating'].widget.attrs['class'] = (
            'rounded-15 text-center form-review')
