# Generated by Django 5.0 on 2024-01-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_rename_marrital_status_kyc_marital_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]