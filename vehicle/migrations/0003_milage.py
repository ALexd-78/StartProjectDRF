# Generated by Django 4.2.4 on 2023-08-05 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_moto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(default=0, verbose_name='год регистрации пробега')),
                ('milage', models.PositiveSmallIntegerField(default=0, verbose_name='пробег')),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.car')),
                ('moto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.moto')),
            ],
            options={
                'verbose_name': 'пробег',
                'verbose_name_plural': 'пробеги',
            },
        ),
    ]
