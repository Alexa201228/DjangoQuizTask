# Generated by Django 3.2 on 2021-06-04 12:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizEngine', '0007_alter_question_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
