# Generated by Django 4.0.7 on 2023-03-31 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_alter_breed_name_alter_cat_nickname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='weigth',
            new_name='weight',
        ),
    ]