# Generated by Django 3.2.7 on 2021-10-04 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
