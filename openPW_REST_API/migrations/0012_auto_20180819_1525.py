# Generated by Django 2.1 on 2018-08-19 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openPW_REST_API', '0011_auto_20180819_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productexchange',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productexchange',
            name='target_company',
        ),
    ]