# Generated by Django 2.1 on 2018-08-22 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openPW_REST_API', '0019_auto_20180821_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, to='openPW_REST_API.Company'),
        ),
    ]
