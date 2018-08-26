# Generated by Django 2.1 on 2018-08-26 11:46

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('openPW_REST_API', '0023_auto_20180825_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traderequest',
            name='trade_trans',
        ),
        migrations.AddField(
            model_name='traderequest',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='openPW_REST_API.Product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderequest',
            name='requesting_company',
            field=models.CharField(default=datetime.datetime(2018, 8, 26, 11, 45, 56, 349969, tzinfo=utc), max_length=90),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderequest',
            name='target_product',
            field=models.CharField(default=None, max_length=90),
            preserve_default=False,
        ),
    ]