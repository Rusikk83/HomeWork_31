# Generated by Django 4.2 on 2023-05-05 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0011_selection'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='selection',
            options={'verbose_name': 'Подборка', 'verbose_name_plural': 'Подборки'},
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(default='member', max_length=15),
        ),
    ]
