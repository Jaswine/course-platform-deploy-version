# Generated by Django 4.2.5 on 2023-11-18 05:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]