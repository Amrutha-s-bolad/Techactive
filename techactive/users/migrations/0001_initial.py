# Generated by Django 4.2 on 2023-04-13 05:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
