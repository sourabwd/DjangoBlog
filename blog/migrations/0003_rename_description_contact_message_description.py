# Generated by Django 3.2.4 on 2021-06-28 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='description',
            new_name='message_description',
        ),
    ]
