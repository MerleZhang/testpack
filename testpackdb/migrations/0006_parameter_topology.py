# Generated by Django 2.0 on 2020-04-30 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpackdb', '0005_auto_20200429_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('value', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('value', models.TextField(null=True)),
            ],
        ),
    ]
