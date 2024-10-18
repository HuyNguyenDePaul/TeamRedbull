from django.contrib import admin
from django.urls import path
from fx_app import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # Home page view
    path('fx-rates/', views.fx_rate_view, name='fx_rates'),  # FX rates view
    path('currency-converter/', views.currency_converter_view, name='currency_converter'),  # Currency converter view
]
