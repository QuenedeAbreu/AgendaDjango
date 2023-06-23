# Generated by Django 4.2.2 on 2023-06-23 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agenda', '0011_alter_anotacao_compromisso_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotacao_compromisso',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
