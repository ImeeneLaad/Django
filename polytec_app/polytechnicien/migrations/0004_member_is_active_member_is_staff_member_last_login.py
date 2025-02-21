# Generated by Django 5.1.6 on 2025-02-21 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polytechnicien', '0003_member_password_alter_member_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='member',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
