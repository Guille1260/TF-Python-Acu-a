# Generated by Django 5.1.4 on 2025-01-03 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppScholl', '0005_alter_perfil_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(blank=True, default='https://sollentunatrafikskola.se/wp-content/uploads/2018/12/male-feature.jpg', null=True, upload_to='foto_perfil/'),
        ),
    ]
