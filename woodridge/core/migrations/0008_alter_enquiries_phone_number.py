# Generated by Django 4.1.2 on 2022-12-15 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_enquiries_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiries',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]