# Generated by Django 4.2.2 on 2023-06-27 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0016_alter_anotacao_compromisso_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='locais'),
        ),
    ]
