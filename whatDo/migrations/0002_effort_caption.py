# Generated by Django 3.0.4 on 2020-03-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatDo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='effort',
            name='caption',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
