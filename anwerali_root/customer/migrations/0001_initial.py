# Generated by Django 5.0.6 on 2024-05-29 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('customer_phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('customer_experience', models.TextField(verbose_name='Опыт')),
            ],
        ),
    ]
