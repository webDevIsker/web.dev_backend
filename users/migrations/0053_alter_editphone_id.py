# Generated by Django 3.2.9 on 2022-03-04 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0052_alter_editphone_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editphone',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]