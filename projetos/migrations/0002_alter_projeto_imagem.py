# Generated by Django 4.0.6 on 2022-07-28 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='imagem',
            field=models.CharField(max_length=100),
        ),
    ]