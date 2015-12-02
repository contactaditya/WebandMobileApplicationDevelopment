from django import forms
# Send POST request

class NameForm(forms.Form):
    city = forms.CharField(label='city', max_length=100)
    bar = forms.BooleanField(required=False, label='bar')
    coffee = forms.BooleanField(required=False, label='coffee')
    restaurant = forms.BooleanField(required=False, label='restaurant')
    term = forms.CharField(label='term', max_length=100,required=False)

    art = forms.BooleanField(required=False, label='art')
    fashion = forms.BooleanField(required=False, label='fashion')
    film = forms.BooleanField(required=False, label='film')
    holiday = forms.BooleanField(required=False, label='holiday')
    music = forms.BooleanField(required=False, label='music')
    shopping = forms.BooleanField(required=False, label='shopping')
    sports = forms.BooleanField(required=False, label='sports')
    outdoor = forms.BooleanField(required=False, label='outdoor')
    acti = forms.CharField(label='acti',max_length=100,required=False)

    trend = forms.BooleanField(required=False,label='trend')


