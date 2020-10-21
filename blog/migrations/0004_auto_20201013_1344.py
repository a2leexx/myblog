# Generated by Django 3.1.1 on 2020-10-13 13:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tag_publication_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='publication_date',
        ),
        migrations.AddField(
            model_name='article',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
