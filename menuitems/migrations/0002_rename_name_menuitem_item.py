# Generated by Django 4.1.7 on 2023-02-14 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuitems', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='name',
            new_name='item',
        ),
    ]