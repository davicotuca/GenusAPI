# Generated by Django 3.2.15 on 2022-10-21 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_parametros_generations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametros',
            name='WAA',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parametros',
            name='WAa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parametros',
            name='Waa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parametros',
            name='generation_bottleneck',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parametros',
            name='h',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parametros',
            name='pop_bottleneck',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parametros',
            name='pop_size',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parametros',
            name='s',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parametros',
            name='u',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
    ]
