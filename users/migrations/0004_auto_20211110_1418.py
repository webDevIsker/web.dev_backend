# Generated by Django 3.2.9 on 2021-11-10 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_loglist_vacations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loglist',
            options={'verbose_name': 'LogList', 'verbose_name_plural': 'LogList'},
        ),
        migrations.AlterModelOptions(
            name='vacations',
            options={'verbose_name': 'Заявки на отпуск', 'verbose_name_plural': 'Заявки на отпуск'},
        ),
    ]
