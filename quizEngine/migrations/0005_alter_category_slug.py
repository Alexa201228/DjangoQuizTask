# Generated by Django 3.2 on 2021-05-31 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizEngine', '0004_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
