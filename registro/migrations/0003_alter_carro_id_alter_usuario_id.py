# Generated by Django 5.1 on 2024-09-04 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_alter_tipo_v_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
