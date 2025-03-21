# Generated by Django 5.1.7 on 2025-03-08 13:23

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('BirthDate', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['FirstName', 'LastName'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('summary', models.TextField()),
                ('isbin', models.CharField(max_length=50, unique=True, verbose_name='ISBiN')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cataloge.author')),
                ('genre', models.ManyToManyField(to='cataloge.genre')),
                ('lang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cataloge.lang')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('inprint', models.CharField(max_length=1000)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', max_length=20)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cataloge.book')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
    ]
