# Generated by Django 3.2.9 on 2022-02-02 06:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0045_alter_loglist_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formsmaws',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
