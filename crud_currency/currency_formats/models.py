from django.db import models

# Create your models here.


class Country(models.Model):
    country_name = models.CharField(max_length=50)
    country_currency = models.CharField(max_length=50)
    country_code = models.CharField(max_length=4)

    class Meta:
        ordering = ['country_name']

    def __str__(self):
        return self.country_name


class CurrencyFormat(models.Model):
    display_simbol = models.BooleanField(default=False)
    currency_before = models.BooleanField(default=False)
    show_cents = models.BooleanField(default=False)
    thousand_delimiter = models.CharField(max_length=2)
    decimal_delimiter = models.CharField(max_length=2)
    country_name = models.CharField(max_length=50)
    country_currency = models.CharField(max_length=50)
    symbol = models.CharField(max_length=4)

    def __str__(self):
        return self.country_name + '-' + self.country_name


class Advertise(models.Model):
    base_currency = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    value = models.IntegerField(default=0)
