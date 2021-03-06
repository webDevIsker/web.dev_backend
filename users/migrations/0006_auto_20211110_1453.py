# Generated by Django 3.2.9 on 2021-11-10 09:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20211110_1421'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loglist',
            options={'verbose_name': 'Список логов', 'verbose_name_plural': 'Список логов'},
        ),
        migrations.AlterField(
            model_name='loglist',
            name='id_user',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='Идентификатор пользователя'),
        ),
        migrations.AlterField(
            model_name='vacations',
            name='end_vacation',
            field=models.DateField(null=True, verbose_name='Окончание отпуска'),
        ),
        migrations.AlterField(
            model_name='vacations',
            name='id_user',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='Идентификатор пользователя'),
        ),
        migrations.AlterField(
            model_name='vacations',
            name='start_vacation',
            field=models.DateField(null=True, verbose_name='Начало отпуска'),
        ),
    ]
