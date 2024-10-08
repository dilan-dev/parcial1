# Generated by Django 4.2.6 on 2024-09-05 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organizador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=15)),
                ('direccion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha', models.DateTimeField()),
                ('capacidad', models.PositiveBigIntegerField()),
                ('lugar', models.CharField(max_length=255)),
                ('estado', models.CharField(choices=[('activo', 'Activo'), ('cancelado', 'Cancelado'), ('finalizado', 'Finalizado')], default='activo', max_length=20)),
                ('organizador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.organizador')),
            ],
        ),
    ]
