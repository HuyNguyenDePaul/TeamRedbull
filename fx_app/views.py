import requests
from django.shortcuts import render
from .forms import CurrencyConverterForm  # Ensure this form is defined correctly
from decimal import Decimal  # Import Decimal to handle currency calculations


def home_view(request):
    return render(request, 'fx_app/home.html')


# FX Rate View
def fx_rate_view(request):
    url = "https://v6.exchangerate-api.com/v6/30107c15500d7f1b7fc51c91/latest/USD"
    response = requests.get(url)
    
    if response.status_code == 200:  # Check if the request was successful
        data = response.json()  # Convert the API response to JSON
        fx_rates = data.get('conversion_rates', {})  # Extract the rates
    else:
        fx_rates = {}  # Set to an empty dict if API fails

    return render(request, 'fx_app/rates.html', {'fx_rates': fx_rates})


# Currency Converter View
def currency_converter_view(request):
    # Fetch the exchange rates
    url = "https://v6.exchangerate-api.com/v6/30107c15500d7f1b7fc51c91/latest/USD"
    response = requests.get(url)
    
    if response.status_code == 200:  # Check if the request was successful
        data = response.json()  # Convert the API response to JSON
        fx_rates = data.get('conversion_rates', {})  # Extract the rates
    else:
        fx_rates = {}  # Set to an empty dict if API fails

    form = CurrencyConverterForm(request.POST or None)
    converted_amount = None
    from_currency = to_currency = None

    if request.method == 'POST' and form.is_valid():
        amount = Decimal(form.cleaned_data['amount'])  # Convert to Decimal
        from_currency = form.cleaned_data['from_currency'].upper()
        to_currency = form.cleaned_data['to_currency'].upper()

        # Fetch conversion rate from API
        api_url = f"https://v6.exchangerate-api.com/v6/30107c15500d7f1b7fc51c91/pair/{from_currency}/{to_currency}"
        response = requests.get(api_url)
        
        if response.status_code == 200:  # Check if the request was successful
            data = response.json()
            conversion_rate = Decimal(data.get('conversion_rate', 1))  # Convert to Decimal
            converted_amount = amount * conversion_rate  # Perform multiplication with Decimals
        else:
            conversion_rate = Decimal('1')  # Default to 1 if API fails
            converted_amount = amount  # No conversion in this case

    return render(request, 'fx_app/converter.html', {
        'form': form,
        'converted_amount': converted_amount,
        'fx_rates': fx_rates,  # Pass the exchange rates to the template
        'from_currency': from_currency,
        'to_currency': to_currency,
    })
