# Generated by Django 2.2.3 on 2020-08-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destinos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50, verbose_name='lugar')),
                ('description', models.CharField(max_length=100, verbose_name='descripcion')),
                ('images', models.ImageField(upload_to='viajes/images')),
                ('recommended', models.CharField(max_length=2, verbose_name='recomendado')),
                ('comments', models.TextField(max_length=200, verbose_name='comentarios')),
                ('weather', models.TextField(max_length=100, verbose_name='clima')),
            ],
        ),
    ]