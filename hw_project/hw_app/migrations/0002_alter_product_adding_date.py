# Generated by Django 5.0.1 on 2024-01-19 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='adding_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]