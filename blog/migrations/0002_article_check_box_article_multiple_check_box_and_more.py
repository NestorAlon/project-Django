# Generated by Django 5.1.3 on 2024-11-14 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='check_box',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='multiple_check_box',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='pulldown',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='radio',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
