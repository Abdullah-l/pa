# Generated by Django 2.2.6 on 2019-10-28 16:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_auto_20191027_1202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='url',
            new_name='trackId',
        ),
        migrations.AddField(
            model_name='episode',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
