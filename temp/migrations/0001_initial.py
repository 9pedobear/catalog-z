# Generated by Django 4.0.4 on 2022-05-12 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('choice', models.CharField(blank=True, choices=[(1, 'Python'), (2, 'Java')], max_length=255)),
                ('text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='files/%Y/%m/%d')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('views', models.IntegerField(blank=True)),
                ('license', models.TextField(blank=True)),
                ('dimension', models.CharField(blank=True, max_length=255)),
                ('format', models.CharField(blank=True, max_length=255)),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='temp.tags')),
            ],
        ),
    ]
