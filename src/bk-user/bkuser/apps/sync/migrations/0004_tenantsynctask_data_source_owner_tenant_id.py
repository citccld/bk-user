# Generated by Django 3.2.20 on 2024-05-23 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sync', '0003_auto_20240515_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenantsynctask',
            name='data_source_owner_tenant_id',
            field=models.CharField(default='', max_length=128, verbose_name='数据源所有者租户 ID'),
        ),
    ]
