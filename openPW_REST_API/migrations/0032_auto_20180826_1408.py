# Generated by Django 2.1 on 2018-08-26 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openPW_REST_API', '0031_auto_20180826_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrequest',
            name='product',
            field=models.IntegerField(max_length=9),
        ),
        migrations.AlterField(
            model_name='productrequest',
            name='requesting_company',
            field=models.IntegerField(max_length=9),
        ),
    ]