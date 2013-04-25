from django import forms
from photos.models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
