# Generated by Django 4.1.7 on 2023-03-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0003_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
