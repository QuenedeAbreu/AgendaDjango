# Generated by Django 4.2.2 on 2023-06-27 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0017_local_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='compromisso',
            name='registro',
            field=models.FileField(blank=True, null=True, upload_to='arquivos'),
        ),
        migrations.AlterField(
            model_name='local',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='ft_locais'),
        ),
    ]