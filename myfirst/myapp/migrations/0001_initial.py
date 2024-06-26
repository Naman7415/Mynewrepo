# Generated by Django 5.0.3 on 2024-03-14 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TenantModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant1Model',
            fields=[
                ('tenantmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.tenantmodel')),
            ],
            options={
                'db_table': 'tenant1_model',
            },
            bases=('myapp.tenantmodel',),
        ),
        migrations.CreateModel(
            name='Tenant2Model',
            fields=[
                ('tenantmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.tenantmodel')),
            ],
            options={
                'db_table': 'tenant2_model',
            },
            bases=('myapp.tenantmodel',),
        ),
    ]
