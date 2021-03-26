from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'currencyFormats'
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^api/currencyFormats/list$', views.list_currency_format),
    url(r'^api/currencyFormats/create$', views.create_currency_format),
    url(r'^api/currencyFormats/delete$', views.delete_all_currency_format),
    url(r'^api/currencyFormats/detail/(?P<pk>[0-9]+)$',
        views.detail_currency_format),
    url(r'^api/currencyFormats/update/(?P<pk>[0-9]+)$',
        views.update_currency_format),
    url(r'^api/currencyFormats/delete/(?P<pk>[0-9]+)$',
        views.delete_currency_format),
    url(r'^api/currencyFormats/countries$', views.currency_by_country)
]
