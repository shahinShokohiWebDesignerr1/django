# Generated by Django 5.1 on 2024-09-06 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_rename_approach_comment_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created_at',)},
        ),
    ]
