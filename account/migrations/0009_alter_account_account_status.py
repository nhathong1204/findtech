# Generated by Django 5.0 on 2024-01-03 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_kyc_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_status',
            field=models.CharField(choices=[('active', 'Active'), ('pending', 'Pending'), ('in-active', 'In Active')], default='in-active', max_length=100),
        ),
    ]
