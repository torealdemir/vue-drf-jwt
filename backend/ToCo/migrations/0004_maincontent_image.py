# Generated by Django 5.0.3 on 2024-04-22 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToCo', '0003_remove_maincontent_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='maincontent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]