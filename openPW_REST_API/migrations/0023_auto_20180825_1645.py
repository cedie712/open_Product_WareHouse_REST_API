# Generated by Django 2.1 on 2018-08-25 16:45

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('openPW_REST_API', '0022_productexchange_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='productexchange',
            name='trans_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traderequest',
            name='trans_datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 25, 16, 45, 58, 696898, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
