# Generated by Django 4.2.9 on 2024-01-28 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_publish_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_at',
            field=models.DateTimeField(null=True),
        ),
    ]
