# Generated by Django 5.0.6 on 2024-07-01 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pointage', '0002_rename_id_code_id_alter_employe_familiy_situation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='code',
            old_name='Description',
            new_name='description',
        ),
    ]
