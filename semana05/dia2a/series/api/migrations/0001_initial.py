# Generated by Django 4.0.6 on 2022-07-14 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0)),
                ('categoria', models.CharField(choices=[('horror', 'Horror'), ('comedia', 'Comedia'), ('accion', 'Accion'), ('drama', 'Drama')], max_length=10)),
            ],
        ),
    ]
