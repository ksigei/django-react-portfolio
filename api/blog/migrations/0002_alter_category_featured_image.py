# Generated by Django 4.2.3 on 2023-07-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/category'),
        ),
    ]
