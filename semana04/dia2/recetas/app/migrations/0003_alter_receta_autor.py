# Generated by Django 4.0.6 on 2022-07-06 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.autor'),
        ),
    ]
