# Generated by Django 5.1.4 on 2025-01-03 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppScholl', '0004_alter_perfil_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='foto_perfil/'),
        ),
    ]
