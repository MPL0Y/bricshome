# Generated by Django 3.0.6 on 2020-06-15 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_event_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_abstract',
            field=models.TextField(default='Lorem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='history_abstract',
            field=models.TextField(default='Lorem'),
            preserve_default=False,
        ),
    ]
