# Generated by Django 5.1.4 on 2025-01-13 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='null', max_length=128),
            preserve_default=False,
        ),
    ]
