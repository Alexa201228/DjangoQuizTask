from django.urls import path
from . import views

app_name = 'quizEngine'

urlpatterns = [
    path('', views.welcome_view, name="welcome"),
    path('<slug:category>/',
         views.quiz_list,
         name='quiz_list'),
    path('<slug:category>/result/',
         views.quiz_save_result,
         name='quiz_save_result'),

]
