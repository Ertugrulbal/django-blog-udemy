# Generated by Django 3.1.5 on 2021-10-25 10:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_yazilarmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazilarmodel',
            name='icerik',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
