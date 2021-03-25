from django.contrib import admin
from .models import Country, CurrencyFormat, Advertise

# Register your models here.

admin.site.register(Country)
admin.site.register(CurrencyFormat)
admin.site.register(Advertise)
