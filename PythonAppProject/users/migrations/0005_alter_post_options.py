# Generated by Django 3.2.6 on 2022-01-08 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_post_meet_day'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-meet_day']},
        ),
    ]
