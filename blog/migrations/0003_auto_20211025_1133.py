# Generated by Django 3.1.5 on 2021-10-25 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211025_1113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategorimodel',
            options={'verbose_name': 'Kategori', 'verbose_name_plural': 'Kategoriler'},
        ),
        migrations.AlterModelTable(
            name='kategorimodel',
            table='kategori',
        ),
    ]
