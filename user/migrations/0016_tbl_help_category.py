# Generated by Django 4.2.16 on 2025-04-29 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_tbl_principal'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_help',
            name='Category',
            field=models.CharField(max_length=90, null=True),
        ),
    ]
