# Generated by Django 4.2.11 on 2024-04-17 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
                ('confirm_password', models.CharField(max_length=20)),
            ],
        ),
    ]