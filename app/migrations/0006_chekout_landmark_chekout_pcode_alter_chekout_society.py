# Generated by Django 4.1.7 on 2023-04-03 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_chekout'),
    ]

    operations = [
        migrations.AddField(
            model_name='chekout',
            name='landmark',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chekout',
            name='pcode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chekout',
            name='society',
            field=models.CharField(max_length=20),
        ),
    ]
