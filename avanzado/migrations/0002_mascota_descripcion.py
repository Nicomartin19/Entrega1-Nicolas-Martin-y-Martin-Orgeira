# Generated by Django 4.1.2 on 2022-11-10 14:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avanzado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
