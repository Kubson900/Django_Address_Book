# Generated by Django 3.2.4 on 2021-07-04 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0004_auto_20210704_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='zip_code',
            field=models.CharField(default='', max_length=12, verbose_name='Postal Code'),
        ),
    ]
