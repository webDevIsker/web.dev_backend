# Generated by Django 3.2.9 on 2022-03-04 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0049_editemails_editphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editphone',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
