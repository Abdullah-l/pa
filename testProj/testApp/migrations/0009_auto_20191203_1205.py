# Generated by Django 3.0b1 on 2019-12-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0008_timeline_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='caption',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='credit',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]