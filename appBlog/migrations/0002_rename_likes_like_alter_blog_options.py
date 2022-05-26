# Generated by Django 4.0.3 on 2022-05-26 16:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appBlog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Likes',
            new_name='Like',
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-publish_date'], 'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
    ]
