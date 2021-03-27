from rest_framework import serializers
from .models import Advertise, Country, CurrencyFormat


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


class AdvertiseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertise
        fields = ('id',
                  'base_currency',
                  'name',
                  'value',
                  'valueText'
                  )


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id',
                  'country_name',
                  'country_currency',
                  'country_code'
                  )
