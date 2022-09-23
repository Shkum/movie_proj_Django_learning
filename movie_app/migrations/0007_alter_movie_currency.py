# Generated by Django 4.1 on 2022-09-23 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_movie_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('EUR', 'Euro'), ('USD', 'Dollar'), ('UAH', 'Hryvna')], default='EUR', max_length=3),
        ),
    ]