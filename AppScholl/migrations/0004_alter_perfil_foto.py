# Generated by Django 5.1.4 on 2025-01-03 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppScholl', '0003_perfil_delete_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(null=True, upload_to='foto_perfil/'),
        ),
    ]
