# Generated by Django 3.2.6 on 2022-02-24 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_invoice_csv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.email'),
        ),
    ]
