# Generated by Django 5.1 on 2024-08-25 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_rename_catagory_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='catagory',
            new_name='category',
        ),
    ]
