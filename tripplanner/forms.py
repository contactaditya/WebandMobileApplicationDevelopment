from django import forms


# Send POST request


class NameForm(forms.Form):
    city = forms.CharField(label='City', max_length=100)
    term = forms.CharField(label='Term', max_length=100)