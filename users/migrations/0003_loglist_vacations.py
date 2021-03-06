# Generated by Django 3.2.9 on 2021-11-10 09:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211110_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('id_user', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('id_num', models.CharField(blank=True, default='000000000000', max_length=15, null=True, verbose_name='ИИН')),
                ('first_name', models.CharField(max_length=250, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=250, verbose_name='Фамилия')),
                ('full_name', models.CharField(max_length=250, verbose_name='Организация')),
                ('doc_name', models.CharField(max_length=250, verbose_name='Название документа')),
                ('doc_date', models.DateTimeField(null=True, verbose_name='Дата создания')),
                ('doc_status', models.CharField(max_length=250, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='Vacations',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('doc_name', models.CharField(max_length=250, verbose_name='Название документа')),
                ('id_user', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('id_num', models.CharField(blank=True, default='000000000000', max_length=15, null=True, verbose_name='ИИН')),
                ('first_name', models.CharField(max_length=250, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=250, verbose_name='Фамилия')),
                ('full_name', models.CharField(max_length=250, verbose_name='Организация')),
                ('start_vacation', models.DateTimeField(null=True, verbose_name='Начало отпуска')),
                ('end_vacation', models.DateTimeField(null=True, verbose_name='Окончание отпуска')),
                ('doc_date', models.DateTimeField(null=True, verbose_name='Дата создания')),
                ('vacation_status', models.CharField(max_length=250, verbose_name='Статус')),
            ],
        ),
    ]
