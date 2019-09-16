from django import forms
from django.forms import widgets
from webapp.models import status_choices


class ArticleForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Description')
    total_description = forms.CharField(max_length=3000, required=True, widget=widgets.Textarea, label='total_description')
    status = forms.ChoiceField(choices=status_choices, required=False, label='Status',)
    date = forms.DateField(label='date', widget=widgets.DateInput(attrs={'type': 'date'}))
