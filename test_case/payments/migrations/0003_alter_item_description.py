# Generated by Django 4.1.1 on 2022-09-14 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='Описание'),
        ),
    ]
