# Generated by Django 3.2.9 on 2022-02-02 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0038_auto_20220201_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loglist',
            name='line_manager',
            field=models.CharField(default='', max_length=250, null=True, verbose_name='Line Manager'),
        ),
    ]