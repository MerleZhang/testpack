# Generated by Django 2.0 on 2020-05-10 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testpackdb', '0012_project_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='case',
            new_name='maps',
        ),
    ]
