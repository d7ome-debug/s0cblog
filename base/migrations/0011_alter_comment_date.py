# Generated by Django 5.0.1 on 2024-01-23 19:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
