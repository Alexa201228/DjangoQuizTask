from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField
import re


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name

    def get_questions(self):
        return self.quiz_questions.all()

    class Meta:
        verbose_name_plural = 'Categories'


class Question(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='quiz_questions',
                                 on_delete=models.CASCADE,
                                 default='')

    question = RichTextField(blank=True, null=True)
    num_of_answers = models.IntegerField(
        help_text="value should be from 1 to 4",
        validators=[MinValueValidator(1), 
                    MaxValueValidator(4)]
        )

    def __str__(self):
        return self.question_name()[:100] + "..."

    def question_name(self):
        question_pattern = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        question_text = re.sub(question_pattern, "", str(self.question))
        return question_text

    def get_answers(self):
        return self.answers.all()

    def correct_answers(self):
        answers = self.get_answers().filter(is_correct=True)
        return answers


class Answer(models.Model):
    question_key = models.ForeignKey(Question,
                                     related_name='answers',
                                     on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
