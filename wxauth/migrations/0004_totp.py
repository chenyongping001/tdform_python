# Generated by Django 3.2.9 on 2022-05-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxauth', '0003_hfwxuser_can_add'),
    ]

    operations = [
        migrations.CreateModel(
            name='TOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=255)),
                ('isuser', models.CharField(blank=True, max_length=255, null=True)),
                ('remark', models.CharField(blank=True, max_length=255, null=True)),
                ('secret', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
