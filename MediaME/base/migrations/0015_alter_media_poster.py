# Generated by Django 5.1.7 on 2025-04-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_merge_20250408_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
