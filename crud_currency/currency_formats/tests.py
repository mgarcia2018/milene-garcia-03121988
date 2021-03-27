from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
import json
from rest_framework.test import APITestCase
from rest_framework import status

from . import views

# Create your tests here.


class AdvertiseTests(APITestCase):
    def test_create_advertise(self):
        data = {"thousand_delimiter": ".",
                "decimal_delimiter": ",", "country_name": "GER", "country_currency": "EUR", "symbol": "$"}

        url = 'api/currencyFormats/create'

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_advertise(self):
        c = Client()
        url = 'api/advertise/list'
        response = c.get(url)

        print(response.content)

        self.assertEqual(response.status_code, 200)

    def test_list_currency_format(self):
        c = Client()
        url = 'api/currencyFormats/list'
        response = c.get(url)

        print(response.content)

        self.assertEqual(response.status_code, 200)

    def test_detail_currency_format(self):
        c = Client()
        url = 'api/currencyFormats/detail/1'
        response = c.get(url)

        print(response.content)

        self.assertEqual(response.status_code, 200)
