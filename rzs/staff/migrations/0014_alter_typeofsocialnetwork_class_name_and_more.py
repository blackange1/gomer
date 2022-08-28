# Generated by Django 4.1 on 2022-08-18 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0013_alter_typeofsocialnetwork_class_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeofsocialnetwork',
            name='class_name',
            field=models.CharField(help_text='назви класів шукайте за посиланням https://fortawesome.com/sets/font-awesome-5-brands or https://fontawesome.com/', max_length=32, unique=True, verbose_name="ім'я класу"),
        ),
        migrations.AlterField(
            model_name='typeofsocialnetwork',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='назва'),
        ),
    ]
