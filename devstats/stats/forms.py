# django imports
from django import forms

# project imports
from stats.models import Developer


class DeveloperCreateForm(forms.ModelForm):
    def clean_username(self):
        # return username in lowercase
        return self.cleaned_data['username'].lower()

    class Meta:
        model = Developer
        fields = ['username']
