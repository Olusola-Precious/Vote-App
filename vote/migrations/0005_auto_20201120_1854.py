# Generated by Django 3.1.3 on 2020-11-20 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0004_auto_20201120_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voters',
            name='vote',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]