# Generated by Django 4.0.4 on 2022-05-05 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_modif', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
