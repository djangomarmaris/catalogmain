# Generated by Django 4.0 on 2023-06-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0022_shot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shot',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%y/%m/%d', verbose_name='652x471'),
        ),
    ]
