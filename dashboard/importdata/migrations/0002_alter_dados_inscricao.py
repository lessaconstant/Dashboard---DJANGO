# Generated by Django 5.0.2 on 2024-04-02 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados',
            name='inscricao',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]