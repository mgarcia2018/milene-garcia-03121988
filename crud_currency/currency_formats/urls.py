from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'currencyFormats'
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^api/currencyFormats$', views.currency_formats_list),
    url(r'^api/currencyFormats/(?P<pk>[0-9]+)$', views.currency_format_detail),
    url(r'^api/currencyFormats/countries$', views.currency_by_country)
]
