# Generated by Django 2.0.2 on 2018-04-13 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20180404_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='content',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='public',
            name='content',
            field=models.TextField(max_length=5000),
        ),
    ]
