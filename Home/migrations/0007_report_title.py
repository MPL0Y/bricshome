# Generated by Django 3.0.6 on 2020-06-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_auto_20200615_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='title',
            field=models.CharField(default='New Website', max_length=200),
            preserve_default=False,
        ),
    ]
