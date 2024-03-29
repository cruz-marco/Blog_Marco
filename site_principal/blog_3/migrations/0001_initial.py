# Generated by Django 4.2.6 on 2023-11-29 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Data de modificação')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Biscoito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Data de modificação')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('Autor', models.CharField(max_length=100)),
                ('Frase', models.TextField(max_length=250)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Adicionado por')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Assuntos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Data de modificação')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('Assunto', models.CharField(max_length=100)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Adicionado por')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
