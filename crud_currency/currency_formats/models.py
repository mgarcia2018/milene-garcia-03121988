from django.db import models

# Create your models here.


class Country(models.Model):
    country_name = models.CharField(max_length=50)
    country_currency = models.CharField(max_length=50)
    country_code = models.CharField(max_length=4)


class CurrencyFormat(models.Model):
    display_simbol = models.BooleanField(default=False)
    currency_before = models.BooleanField(default=False)
    show_cents = models.BooleanField(default=False)
    dot_delimiter = models.BooleanField(default=False)
    country_name = models.CharField(max_length=50)
    country_currency = models.CharField(max_length=50)


class Advertise(models.Model):
    base_currency = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    value = models.IntegerField(default=0)
