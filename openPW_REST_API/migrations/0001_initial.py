# Generated by Django 2.1 on 2018-08-17 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=90, unique=True)),
                ('company_location', models.CharField(max_length=60, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='CompanyHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=90, unique=True)),
                ('product_count', models.IntegerField()),
                ('product_base_price', models.FloatField(max_length=30)),
                ('product_dispatch_price', models.FloatField(max_length=30)),
                ('product_description', models.CharField(default=None, max_length=128)),
                ('date_modified', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openPW_REST_API.Company')),
            ],
        ),
        migrations.CreateModel(
            name='ProductExchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_company', models.CharField(max_length=90)),
                ('target_product', models.CharField(max_length=90)),
                ('is_verified', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openPW_REST_API.Company')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openPW_REST_API.Product')),
            ],
        ),
        migrations.CreateModel(
            name='TradeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openPW_REST_API.Company')),
                ('trade_trans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openPW_REST_API.ProductExchange')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_type', models.CharField(max_length=90)),
                ('trans_date', models.DateTimeField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openPW_REST_API.Company')),
            ],
            options={
                'verbose_name_plural': 'transactionhistories',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openPW_REST_API.Company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='company_head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, to='openPW_REST_API.CompanyHead'),
        ),
    ]