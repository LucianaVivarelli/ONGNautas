# Generated by Django 4.2.3 on 2023-08-03 19:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='Não definido', max_length=64),
        ),
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='cep',
            field=models.CharField(default='Não definido', max_length=11),
        ),
        migrations.AddField(
            model_name='user',
            name='complement',
            field=models.CharField(blank=True, max_length=24),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, default='_', max_length=150),
        ),
    ]
