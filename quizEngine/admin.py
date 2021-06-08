from django.contrib import admin
from .models import Question, Answer, Category


class AnswersInline(admin.StackedInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_name', 'num_of_answers']
    list_per_page = 10
    inlines = [AnswersInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
