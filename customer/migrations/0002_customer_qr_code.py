# Generated by Django 3.2.4 on 2021-06-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='customer_qr_code'),
        ),
    ]
