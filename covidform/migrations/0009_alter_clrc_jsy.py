# Generated by Django 3.2.9 on 2022-05-07 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidform', '0008_clrc_clrcfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clrc',
            name='jsy',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
