# Generated by Django 2.0 on 2020-04-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpackdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='area',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cases',
            name='priority',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='cases',
            name='test_type',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='cases',
            name='topology',
            field=models.CharField(max_length=20),
        ),
    ]