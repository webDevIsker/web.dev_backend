# Generated by Django 3.2.9 on 2022-02-02 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0043_alter_vacations_doc_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loglist',
            name='full_name',
            field=models.CharField(default='', max_length=250, verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='vacations',
            name='full_name',
            field=models.CharField(default='', max_length=250, verbose_name='Организация'),
        ),
    ]
