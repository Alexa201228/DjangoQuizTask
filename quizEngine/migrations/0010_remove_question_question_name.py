# Generated by Django 3.2 on 2021-06-04 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizEngine', '0009_question_question_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_name',
        ),
    ]
