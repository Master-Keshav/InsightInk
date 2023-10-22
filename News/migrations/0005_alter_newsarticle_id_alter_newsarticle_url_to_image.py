# Generated by Django 4.2.5 on 2023-10-22 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0004_alter_newsarticle_url_alter_newsarticle_url_to_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='url_to_image',
            field=models.URLField(max_length=500, unique=True),
        ),
    ]