# Generated by Django 3.2.15 on 2022-10-24 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_simulacao_resultado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulacao',
            name='resultado',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='core.resultados'),
            preserve_default=False,
        ),
    ]
