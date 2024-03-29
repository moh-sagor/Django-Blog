# Generated by Django 3.2.7 on 2021-10-27 16:54

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-publish_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='blog_title'),
        ),
    ]
