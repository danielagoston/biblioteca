# Generated by Django 2.2 on 2024-02-12 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0004_libro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libros.Autor'),
        ),
    ]
