# Generated by Django 4.1 on 2024-11-30 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_refbook_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refbookversion',
            old_name='refbook_id',
            new_name='refbook',
        ),
    ]