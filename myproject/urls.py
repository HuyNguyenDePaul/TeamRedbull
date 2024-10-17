"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fx_app import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fx-rates/', views.fx_rate_view, name='fx_rates'),  # Route for Real-Time FX Rates
    path('currency-converter/', views.currency_converter_view, name='currency_converter'),  # Route for Currency Converter
]
urlpatterns = [
    path('fx-rates/', views.fx_rate_view, name='fx_rates'),
    path('currency-converter/', views.currency_converter_view, name='currency_converter'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # Home page view
    path('fx-rates/', views.fx_rate_view, name='fx_rates'),  # FX rates view
    path('currency-converter/', views.currency_converter_view, name='currency_converter'),  # Currency converter view
]