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
    thousand_delimiter = models.CharField(max_length=2, default=0)
    decimal_delimiter = models.CharField(max_length=2, default=0)
    country_name = models.CharField(max_length=50, default="")
    country_currency = models.CharField(max_length=50, default="")
    symbol = models.CharField(max_length=4, default="")

    def __str__(self):
        return self.country_name + '-' + self.country_currency


class Advertise(models.Model):
    base_currency = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    value = models.DecimalField(default=0, max_digits=10, decimal_places=3)
    valueText = models.CharField(max_length=50, default="0")

    def __str__(self):
        return self.name + '-' + self.base_currency
