from django import forms


class NewList(forms.Form):
    name = forms.CharField(max_length=200, label="List name")
    check = forms.BooleanField(required=False)
