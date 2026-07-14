from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maestro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('materia', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('grado', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
    ]
