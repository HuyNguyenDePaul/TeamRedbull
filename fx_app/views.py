import requests
from django.shortcuts import render
from .forms import CurrencyConverterForm  # Import the form for currency conversion


from django.shortcuts import render

def home_view(request):
    return render(request, 'fx_app/home.html')


# FX Rate View
def fx_rate_view(request):
    url = "https://v6.exchangerate-api.com/v6/30107c15500d7f1b7fc51c91/latest/USD"
    response = requests.get(url)
    data = response.json()  # Convert the API response to JSON
    fx_rates = data.get('conversion_rates', {})  # Extract the rates

    return render(request, 'fx_app/rates.html', {'fx_rates': fx_rates})

# Currency Converter View
def currency_converter_view(request):
    form = CurrencyConverterForm(request.POST or None)
    converted_amount = None
    from_currency = to_currency = None

    if request.method == 'POST' and form.is_valid():
        amount = form.cleaned_data['amount']
        from_currency = form.cleaned_data['from_currency'].upper()
        to_currency = form.cleaned_data['to_currency'].upper()

        # Fetch conversion rate from API
        api_url = f"https://v6.exchangerate-api.com/v6/30107c15500d7f1b7fc51c91/pair/{from_currency}/{to_currency}"
        response = requests.get(api_url)
        data = response.json()
        conversion_rate = data.get('conversion_rate', 1)

        converted_amount = amount * conversion_rate

    return render(request, 'fx_app/converter.html', {
        'form': form,
        'converted_amount': converted_amount,
        'from_currency': from_currency,
        'to_currency': to_currency,
    })
