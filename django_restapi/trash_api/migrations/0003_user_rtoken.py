# Generated by Django 3.0.7 on 2020-06-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trash_api', '0002_auto_20200609_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rtoken',
            field=models.CharField(max_length=256, null=True),
        ),
    ]