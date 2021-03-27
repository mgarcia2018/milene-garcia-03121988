# Generated by Django 3.0.5 on 2021-03-26 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_formats', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Advertise',
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['country_name']},
        ),
        migrations.RemoveField(
            model_name='currencyformat',
            name='dot_delimiter',
        ),
        migrations.AddField(
            model_name='currencyformat',
            name='decimal_delimiter',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='currencyformat',
            name='symbol',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AddField(
            model_name='currencyformat',
            name='thousand_delimiter',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='currencyformat',
            name='country_currency',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='currencyformat',
            name='country_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]