# Generated by Django 2.2 on 2024-02-12 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_auto_20240212_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='apellidos',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='autor',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nacionalidad',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
    ]
