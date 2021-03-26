from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import CurrencyFormat
from .serializers import CurrencyFormatSerializer
from rest_framework.decorators import api_view

# Create your views here.


def index(request):
    currency_list = CurrencyFormat.objects.order_by('country_name')[:5]
    context = {'currency_list': currency_list}
    return render(request, 'currencyFormats/index.html', context)


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

    country = request.GET.get('country_name', None)
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
          description: Json object e.x: {"id": 1, "display_simbol": true, "currency_before": true, "show_cents": true, "thousand_delimiter": ".", "decimal_delimiter": ",", "country_name": "Cuba", "country_currency": "CUP", "symbol": "$"}
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
