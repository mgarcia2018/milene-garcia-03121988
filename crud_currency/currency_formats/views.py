from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Advertise, Country, CurrencyFormat
from .serializers import CountrySerializer, CurrencyFormatSerializer, AdvertiseSerializer
from rest_framework.decorators import api_view

import locale
from decimal import Decimal

# Create your views here.


@api_view(['GET', ])
def list_currency_format(request):
    """
    API Endpoint that return a list of currency formats
    ---
    parameters:
        - name: country
          description: To find a currency format by a country name
          required: false
          paramType: string
    """

    currencyAllData = CurrencyFormat.objects.all()

    country = request.GET.get('country', None)
    if country is not None:
        currencyAllData = currencyAllData.filter(
            country_name__icontains=country)

    currency_serializer = CurrencyFormatSerializer(currencyAllData, many=True)
    return JsonResponse(currency_serializer.data, safe=False)


@api_view(['POST', ])
def create_currency_format(request):
    """
    API Endpoint for create a currency formats

    Parameters:
        - name: request
          description: Json object e.x: {"display_simbol": True, "currency_before": True, "show_cents": True, "thousand_delimiter": ".", "decimal_delimiter": ",", "country_name": "Cuba", "country_currency": "CUP", "symbol": "$"}
          required: true
          paramType: Json Object
    """

    currency_data = JSONParser().parse(request)
    currency_serializer = CurrencyFormatSerializer(data=currency_data)
    if currency_serializer.is_valid():
        currency_serializer.save()
        return JsonResponse(currency_serializer.data, status=status.HTTP_201_CREATED)

    return JsonResponse(currency_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def delete_all_currency_format():
    """
      API Endpoint for delete all currency formats

    """

    count = CurrencyFormat.objects.all().delete()
    return JsonResponse({'message': '{} Currency Formats were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def detail_currency_format(request, pk):
    """
      API Endpoint for get a currency format by id

    """
    currency = CurrencyFormat.objects.get(pk=pk)

    currency_serializer = CurrencyFormatSerializer(currency)
    return JsonResponse(currency_serializer.data)


@api_view(['PUT', ])
def update_currency_format(request, pk):
    """
      API Endpoint for update a currency format by id

    """
    currency = CurrencyFormat.objects.get(pk=pk)

    currency_data = JSONParser().parse(request)
    currency_serializer = CurrencyFormatSerializer(
        currency, data=currency_data)
    if currency_serializer.is_valid():
        currency_serializer.save()
        return JsonResponse(currency_serializer.data)
    return JsonResponse(currency_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_currency_format(request, pk):
    """
      API Endpoint for delete a currency format by id

    """
    currency = CurrencyFormat.objects.get(pk=pk)

    currency.delete()
    return JsonResponse({'message': 'Currency was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def currency_by_country(request, country):
    currency = CurrencyFormat.objects.filter(country_name=country)

    if request.method == 'GET':
        currency_serializer = CurrencyFormatSerializer(currency, many=True)
        return JsonResponse(currency_serializer.data, safe=False)


@api_view(['GET', ])
def list_advertise(request):
    """
    API Endpoint that return a advertise by name

    """

    advertises = Advertise.objects.all()

    name = request.GET.get('name', None)
    if name is not None:
        advertises = advertises.filter(
            name__icontains=name)

    advertise_serializer = AdvertiseSerializer(advertises, many=True)
    return JsonResponse(advertise_serializer.data, safe=False)


@api_view(['POST', ])
def create_advertise(request):
    """
    API Endpoint for create an advertise

    Parameters:
        - name: value
          description: Value of de advertise
          required: true
          paramType: Decimal
        - name: countryName
          description: Country name
          required: true
          paramType: String
        - name: countryCurrency
          description: Country currency
          required: true
          paramType: String
    """

    myJson = JSONParser().parse(request)

    countryName = myJson['countryName']
    countryCurrency = myJson['countryCurrency']
    value = Decimal(myJson['value'])

    currency = CurrencyFormat.objects.get(
        country_name=countryName, country_currency=countryCurrency)

    saved = locale.getlocale()

    locale.setlocale(locale.LC_MONETARY, '')

    if currency is not None:

        if currency.thousand_delimiter is not None:
            locale._override_localeconv["mon_thousands_sep"] = currency.thousand_delimiter

        if currency.decimal_delimiter is not None:
            locale._override_localeconv["mon_decimal_point"] = currency.decimal_delimiter
            locale._override_localeconv["decimal_point"] = currency.decimal_delimiter

        if currency.show_cents == False:
            locale._override_localeconv["frac_digits"] = 0
            locale._override_localeconv["int_frac_digits"] = 0

        if currency.display_simbol == True:
            locale._override_localeconv["currency_symbol"] = currency.symbol
            locale._override_localeconv["int_curr_symbol"] = currency.symbol

        else:
            locale._override_localeconv["currency_symbol"] = currency.country_currency
            locale._override_localeconv["int_curr_symbol"] = currency.country_currency

        locale._override_localeconv["p_cs_precedes"] = currency.currency_before

        formatValue = locale.currency(value)

        locale.setlocale(locale.LC_TIME, saved)

        advertise_data = {"name": "Advertise_" + countryName,
                          "base_currency": countryCurrency, "value": value, "valueText": formatValue}
        advertise_serializer = AdvertiseSerializer(data=advertise_data)
        if advertise_serializer.is_valid():
            advertise_serializer.save()
            return JsonResponse({'result': 'Success', 'status': '201'})

    return JsonResponse({'result': 'error', 'status': '400'})


@api_view(['GET', ])
def list_countries(request):
    """
    API Endpoint that return list of countries

    """

    countries = Country.objects.all()

    name = request.GET.get('name', None)
    if name is not None:
        countries = countries.filter(
            country_name__icontains=name)

    country_serializer = CountrySerializer(countries, many=True)
    return JsonResponse(country_serializer.data, safe=False)
