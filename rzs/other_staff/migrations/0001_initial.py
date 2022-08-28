# Generated by Django 4.1 on 2022-08-23 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0020_person_about_me_person_life_credo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Приклад: Психолог', max_length=64, unique=True, verbose_name='назва (однина)')),
                ('names', models.CharField(help_text='Приклад: Психологи', max_length=64, unique=True, verbose_name='назва (множина)')),
            ],
            options={
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='OtherStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.ManyToManyField(to='other_staff.category', verbose_name='категорії')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staff.person', verbose_name='Працівник')),
            ],
            options={
                'verbose_name_plural': 'Інші працівники',
            },
        ),
    ]