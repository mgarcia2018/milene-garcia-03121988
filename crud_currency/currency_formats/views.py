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


@api_view(['GET', 'POST', 'DELETE'])
def currency_formats_list(request):
    """
    Endpoint returns list of open orders
    ---
    parameters:
        - name: parameter_a
          description: Description for parameter a
          required: true
          paramType: path
        - name: parameter_b
          description: Description for parameter b
          required: true
          paramType: path
    """

    if request.method == 'GET':
        currencyAllData = CurrencyFormat.objects.all()

        country = request.GET.get('country_name', None)
        if country is not None:
            currencyAllData = currencyAllData.filter(
                country_name__icontains=country)

        currency_serializer = CurrencyFormatSerializer(
            currencyAllData, many=True)
        return JsonResponse(currency_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        currency_data = JSONParser().parse(request)
        currency_serializer = CurrencyFormatSerializer(data=currency_data)
        if currency_serializer.is_valid():
            currency_serializer.save()
            return JsonResponse(currency_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(currency_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = CurrencyFormat.objects.all().delete()
        return JsonResponse({'message': '{} Currency Formats were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def currency_format_detail(request, pk):
    currency = CurrencyFormat.objects.get(pk=pk)

    if request.method == 'GET':
        currency_serializer = CurrencyFormatSerializer(currency)
        return JsonResponse(currency_serializer.data)

    elif request.method == 'PUT':
        currency_data = JSONParser().parse(request)
        currency_serializer = CurrencyFormatSerializer(
            currency, data=currency_data)
        if currency_serializer.is_valid():
            currency_serializer.save()
            return JsonResponse(currency_serializer.data)
        return JsonResponse(currency_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        currency.delete()
        return JsonResponse({'message': 'Currency was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def currency_by_country(request, country):
    currency = CurrencyFormat.objects.filter(country_name=country)

    if request.method == 'GET':
        currency_serializer = CurrencyFormatSerializer(currency, many=True)
        return JsonResponse(currency_serializer.data, safe=False)
