# Generated by Django 3.2.15 on 2022-10-24 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20221021_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulacao',
            name='resultado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.resultados'),
        ),
    ]
