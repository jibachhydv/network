# Generated by Django 3.2.3 on 2021-07-12 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0002_likemodel_one like for one user in each post'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comment',
            table='Post Comment',
        ),
        migrations.AlterModelTable(
            name='likemodel',
            table='Post Like',
        ),
        migrations.AlterModelTable(
            name='post',
            table='Post',
        ),
    ]
