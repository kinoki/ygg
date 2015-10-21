from django import forms
from info.models import Detail


class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['name', ]
