from django import template

register = template.Library()

@register.filter
def get_question_index(value, arg):
    return list(value.get_questions()).index(arg) + 1