from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from typing import List


class QuizResultService():
    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto

    def get_result(self) -> float:
        if self.quiz_dto.uuid != self.answers_dto.quiz_uuid:
            raise Exception("Answers don't relate to this quiz")  
        questions = list(self.quiz_dto.questions)
        answers = list(self.answers_dto.answers)

        chosen_answers = {}
        question_answers = {}
        
        for i in questions:
            question_answers[i.uuid] = i.choices
        for i in answers:
            chosen_answers[i.question_uuid] = i.choices

        score = 0

        for i in question_answers.keys():
            if chosen_answers[i] != []:
                correct_answers = []
                for j in question_answers[i]:
                    if j.is_correct:
                        correct_answers.append(j.uuid)
                for ans in chosen_answers[i]:
                    if len(chosen_answers[i]) < len(correct_answers) or ans not in correct_answers:
                        break
                else:
                    score += 1

        result = score / len(questions)

        return result
