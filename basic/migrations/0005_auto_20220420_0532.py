# Generated by Django 3.2.13 on 2022-04-20 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0004_cover_vehicle_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='cover',
            name='fuel_type',
            field=models.CharField(blank=True, choices=[('Cng/lpg', 'Cng/lpg'), ('petrol', 'petrol'), ('elec', 'elec'), ('all', 'all')], default='all', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cover',
            name='owner',
            field=models.CharField(blank=True, choices=[('individual', 'individual'), ('company', 'company'), ('all', 'all')], default='all', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cover',
            name='policy_type',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('comp', 'comp'), ('tp', 'tp'), ('od', 'od'), ('all', 'all')], default='all', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cover',
            name='value_type',
            field=models.CharField(blank=True, choices=[('radio', 'radio'), ('dropdown', 'dropdown'), ('null', 'null')], default='null', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cover',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('FW', 'FW'), ('TW', 'TW'), ('GCV', 'GCV'), ('PCV', 'PCV'), ('all', 'all')], default='all', max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sub_question', models.ManyToManyField(blank=True, to='basic.SubQuestion')),
            ],
        ),
    ]
