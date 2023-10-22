# Generated by Django 4.2.5 on 2023-10-22 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_newsarticle_id_alter_newsarticle_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='url_to_image',
            field=models.URLField(max_length=500),
        ),
    ]
