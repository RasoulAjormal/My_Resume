# Generated by Django 3.2.13 on 2022-06-26 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('About_Me', '0004_auto_20220626_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsofothersmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Comments Of Others'),
        ),
    ]