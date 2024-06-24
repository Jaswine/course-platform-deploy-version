# Generated by Django 4.2.5 on 2023-11-18 04:49

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
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scores', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, default=None, upload_to='profiles')),
                ('backImage', models.ImageField(blank=True, default=None, upload_to='back_images')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=168)),
                ('Twitter', models.CharField(blank=True, max_length=1000)),
                ('GitHub', models.CharField(blank=True, max_length=1000)),
                ('GitLub', models.CharField(blank=True, max_length=1000)),
                ('Linkedin', models.CharField(blank=True, max_length=1000)),
                ('Telegram', models.CharField(blank=True, max_length=1000)),
                ('website', models.URLField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('interests', models.ManyToManyField(blank=True, to='user.interest')),
                ('skills', models.ManyToManyField(blank=True, to='user.skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
