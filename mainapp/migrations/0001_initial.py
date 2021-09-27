# Generated by Django 3.2 on 2021-09-24 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableWebix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='Количество')),
                ('distance', models.PositiveIntegerField(verbose_name='Расстояние')),
            ],
        ),
    ]
