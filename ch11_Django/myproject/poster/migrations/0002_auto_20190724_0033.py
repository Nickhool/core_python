# Generated by Django 2.2 on 2019-07-24 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='publish_at',
            new_name='published_at',
        ),
    ]
