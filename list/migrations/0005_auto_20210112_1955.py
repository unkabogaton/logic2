# Generated by Django 2.2.16 on 2021-01-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item',
            field=models.CharField(max_length=500),
        ),
    ]
