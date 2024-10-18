from django import forms

class CurrencyConverterForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    from_currency = forms.CharField(max_length=3, label="From Currency (e.g., USD)")
    to_currency = forms.CharField(max_length=3, label="To Currency (e.g., EUR)")
