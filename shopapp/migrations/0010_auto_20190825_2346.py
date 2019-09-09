# Generated by Django 2.2.3 on 2019-08-25 17:46

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0009_auto_20190825_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 26, 23, 46, 33, 84975)),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.ForeignKey(default=None, null=True, on_delete='', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 25, 23, 46, 33, 84975)),
        ),
    ]
