# Generated by Django 3.1.1 on 2020-10-15 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_tag_tag_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
