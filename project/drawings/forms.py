from django import forms
from django.core.exceptions import ValidationError
from .models import Notebook

from deluxenation import widgets

class NotebookCreateForm(forms.ModelForm):
    """A form to create a notebook and all the drawigs in it."""

    def clean(self):
        """Clean form data"""
        if not self.files:
            raise ValidationError("No drawings provided for notebook.")
        return super(NotebookCreateForm, self).clean()

    class Meta:
        model = Notebook
        fields = ['title', 'description', 'id', 'drawn_at']
        widgets = {
            'drawn_at': widgets.MonthYearWidget(years=xrange(1980,2050)),

        }
