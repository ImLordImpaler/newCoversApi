# Generated by Django 3.2.13 on 2022-04-21 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0008_auto_20220421_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cover',
            name='owner_type',
            field=models.ManyToManyField(blank=True, default='Individual', to='basic.Owner_type'),
        ),
    ]
