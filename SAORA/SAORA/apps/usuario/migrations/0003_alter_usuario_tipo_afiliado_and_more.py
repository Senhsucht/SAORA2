# Generated by Django 4.2.6 on 2023-10-14 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("usuario", "0002_remove_usuario_activo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="tipo_afiliado",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="usuario.tipoafiliado",
            ),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="tipo_usuario",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="usuario.tipousuario",
            ),
        ),
    ]