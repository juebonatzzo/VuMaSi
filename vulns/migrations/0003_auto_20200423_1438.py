# Generated by Django 2.2.4 on 2020-04-23 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulns', '0002_cve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cve',
            name='cve_id',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]