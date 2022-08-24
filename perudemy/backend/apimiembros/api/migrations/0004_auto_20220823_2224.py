# Generated by Django 3.2 on 2022-08-24 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20220823_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='categoria_id',
            field=models.ForeignKey(db_column='categoria_id', on_delete=django.db.models.deletion.RESTRICT, related_name='Cursos', to='api.categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='miembro',
            name='usuario_id',
            field=models.OneToOneField(db_column='usuario_id', on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]