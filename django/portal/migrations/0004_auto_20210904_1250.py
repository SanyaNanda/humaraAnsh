# Generated by Django 3.2.6 on 2021-09-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_rename_is_teacher_user_is_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='first_name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='patient',
            name='last_name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='patient',
            name='pregnancy_month',
            field=models.IntegerField(default=None),
        ),
    ]
