# Generated by Django 4.1 on 2022-08-20 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0018_alter_person_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.SmallIntegerField(choices=[(0, 'жіноча'), (1, 'чоловіча')], verbose_name='стать'),
        ),
    ]