# Generated by Django 4.0 on 2023-11-30 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20230929_0840'),
        ('strategy_pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArticleMoel',
            new_name='ArticleModel',
        ),
    ]
