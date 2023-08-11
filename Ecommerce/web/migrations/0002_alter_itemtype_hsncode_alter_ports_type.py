# Generated by Django 4.2.4 on 2023-08-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemtype',
            name='HSNcode',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='ports',
            name='type',
            field=models.CharField(choices=[(1, 'dry'), (2, 'sea')], max_length=3),
        ),
    ]
