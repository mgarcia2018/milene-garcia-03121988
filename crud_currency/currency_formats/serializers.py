from rest_framework import serializers
from .models import CurrencyFormat


class CurrencyFormatSerializer(serializers.ModelSerializer):

    class Meta:
        model = CurrencyFormat
        fields = ('id',
                  'display_simbol',
                  'currency_before',
                  'show_cents',
                  'thousand_delimiter',
                  'decimal_delimiter',
                  'country_name',
                  'country_currency',
                  'symbol',
                  )
