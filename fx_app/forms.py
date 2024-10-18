from django import forms

class CurrencyConverterForm(forms.Form):
    from_currency = forms.CharField(label='From Currency', max_length=3)
    to_currency = forms.CharField(label='To Currency', max_length=3)
    amount = forms.DecimalField(label='Amount', max_digits=12, decimal_places=2)
