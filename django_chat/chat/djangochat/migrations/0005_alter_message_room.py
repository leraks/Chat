# Generated by Django 4.0.3 on 2022-03-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangochat', '0004_alter_message_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=10000),
        ),
    ]