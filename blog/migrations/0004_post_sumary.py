# Generated by Django 3.0.8 on 2020-07-14 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200709_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sumary',
            field=models.TextField(default='', verbose_name='Resumo'),
            preserve_default=False,
        ),
    ]
