# Generated by Django 4.0.2 on 2022-06-20 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0016_restaurant_day_restaurant_dayend_restaurant_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(db_index=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_tr',
            field=models.CharField(db_index=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='info_en',
            field=models.TextField(default='Ürün Aaçıklama', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='info_tr',
            field=models.TextField(default='Ürün Aaçıklama', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_tr',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
    ]
