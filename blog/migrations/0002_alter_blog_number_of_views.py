# Generated by Django 5.1.3 on 2025-01-17 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='number_of_views',
            field=models.IntegerField(null=True, verbose_name='колличество просмотров'),
        ),
    ]
