from django import forms
from django.forms import Textarea, TextInput
from django.forms import formset_factory
from django.forms.models import modelformset_factory, inlineformset_factory
from django.forms.models import inlineformset_factory

from models import Drawing, Notebook



class NotebookForm(forms.Form):
    class Meta:
        model = Notebook
        fields = ['id', 'title', 'description']

DrawingFormSet = inlineformset_factory(Notebook, Drawing)

# class DrawingForm(forms.ModelForm):
#     image = forms.ImageField(label='Drawing Image')
#     class Meta:
#         model = Drawing
#         fields = ('image', 'title', 'favorite')

