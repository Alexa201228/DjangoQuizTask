# Generated by Django 3.2 on 2021-06-01 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizEngine', '0006_alter_question_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='quiz_questions', to='quizEngine.category'),
        ),
    ]