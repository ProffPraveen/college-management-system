# Generated by Django 4.2.16 on 2025-04-29 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_tbl_courses_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_principal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal_picture', models.ImageField(null=True, upload_to='static/principal')),
                ('message', models.CharField(max_length=400, null=True)),
                ('principal_name', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
