# Generated by Django 4.0.5 on 2022-06-30 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=210)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('img', models.ImageField(upload_to='vmovi-img/')),
                ('hd', models.CharField(choices=[('HD', 'HD')], max_length=120)),
                ('age_limit', models.CharField(max_length=120)),
                ('year', models.DateField()),
                ('time_run', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=100)),
                ('dic', models.TextField()),
                ('movie_hd', models.FileField(blank=True, null=True, upload_to='video/')),
                ('movie_720', models.FileField(blank=True, null=True, upload_to='video/')),
                ('movie_1440', models.FileField(blank=True, null=True, upload_to='video/')),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField()),
                ('insta', models.URLField()),
                ('twitter', models.URLField()),
            ],
        ),
    ]
