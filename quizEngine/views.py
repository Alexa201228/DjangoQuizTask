from django.urls.base import reverse
from quiz.services import QuizResultService
from quiz.dto import AnswerDTO, AnswersDTO, QuestionDTO, QuizDTO, ChoiceDTO
from django.core import paginator
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import Answer, Question, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def quiz_list(request, category):
    category_id = Category.objects.filter(slug=category)[0]
    questions = Question.objects.filter(category=category_id)
    paginator = Paginator(questions, 1)
    page = request.GET.get('question')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 
                 'quiz/question/question.html',
                 context={'questions': questions,
                          'category': category_id})


def welcome_view(request):
    categories = Category.objects.all()
    return render(request, 'quiz/welcome.html',
                  context={'categories': categories})


def quiz_save_result(request, *args, **kwargs):
    import re
    result = 0
    if request.is_ajax():
        data = dict(request.POST.lists())

        data.pop('csrfmiddlewaretoken')
        category = data.pop('url')[0]

        category_id = Category.objects.filter(slug=category)[0]

        questions = Question.objects.filter(category=category_id)
        temp_data = {}
        for i in data.keys():
            t = re.findall('[0-9]+', i)[0]
            temp_data[t] = data[i]
             
        questions_data = []
        temp_answers = []
        display_correct_answers = []
        display_user_answers = []
        for i in questions:

            user_choice = []
            choices = []

            all_choices = i.get_answers()
            temp_correct_ans = []
            for j in all_choices:
                if j.is_correct:
                    temp_correct_ans.append(j.answer_text)
                ch = ChoiceDTO(str(j.pk), j.answer_text, j.is_correct)

                choices.append(ch)
            display_correct_answers.append(temp_correct_ans)
            temp_user_choice = []
            if str(i.pk) in temp_data.keys():
                for user_ch in temp_data[str(i.pk)]:
                    for choice in choices:
                        if choice.text == user_ch:
                            temp_user_choice.append(choice.text)
                            user_choice.append(choice.uuid)
            
            display_user_answers.append(temp_user_choice)
            answers = AnswerDTO(str(i.pk), user_choice)
            temp = QuestionDTO(str(i.pk), i.question, choices)
            temp_answers.append(answers)
            questions_data.append(temp)

        answers_data = AnswersDTO(str(category_id), temp_answers)
        quiz_data = QuizDTO(str(category_id), category.title(), questions_data)

        calculation = QuizResultService(quiz_data, answers_data)
        result = calculation.get_result()
        result = round(result, 2)
        display_data = zip(questions, display_correct_answers, display_user_answers)
        return render(request, 'quiz/result/results.html',
                      context={"result": result * 100,
                               "questions": display_data,
                               'category': category_id})
    return redirect('quizEngine:welcome')
