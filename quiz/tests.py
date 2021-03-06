from django.test import TestCase
from typing import List
from .services import QuizResultService
from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO


class BaseTestCase(TestCase):
    def setUp(self):
        choices: List[ChoiceDTO] = [
            ChoiceDTO(
                "1-1-1",
                "An elephant",
                True
            ),
            ChoiceDTO(
                "1-1-2",
                "A mouse",
                False
            )
        ]

        questions: List[QuestionDTO] = [
            QuestionDTO(
                "1-1",
                "Who is bigger?",
                choices
            )
        ]

        self.quiz_dto = QuizDTO(
            "1",
            "Animals",
            questions
        )

    def test_success_quiz_result(self):
        answers: List[AnswerDTO] = [
            AnswerDTO(
                "1-1",
                ["1-1-1"]
            )
        ]

        answers_dto = AnswersDTO(
            "1",
            answers
        )

        quiz_result_service = QuizResultService(
            self.quiz_dto,
            answers_dto
        )

        self.assertEqual(quiz_result_service.get_result(), 1.00)

    def test_failure_quiz_result(self):
        answers: List[AnswerDTO] = [
            AnswerDTO(
                "1-1",
                ["1-1-2"]
            )
        ]

        answers_dto = AnswersDTO(
            "1",
            answers
        )

        quiz_result_service = QuizResultService(
            self.quiz_dto,
            answers_dto
        )

        self.assertEqual(quiz_result_service.get_result(), 0.00)

    def test_empty_answer_faitire_quiz_result(self):
        answers: List[AnswerDTO] = [
            AnswerDTO(
                "1-1",
                []
            )
        ]

        answers_dto = AnswersDTO(
            "1",
            answers
        )

        quiz_result_service = QuizResultService(
            self.quiz_dto,
            answers_dto
        )

        self.assertEqual(quiz_result_service.get_result(), 0.00)


class AdvancedQuizTest(TestCase):

    def setUp(self):

        choices1: List[ChoiceDTO] = [
            ChoiceDTO(
                "111",
                "??????????????",
                True
            ),

            ChoiceDTO(
                "112",
                "????????????",
                False
            ),

            ChoiceDTO(
                "113",
                "????????",
                True
            ),

            ChoiceDTO(
                "114",
                "????????????",
                False
            )
        ]

        choices2: List[ChoiceDTO] =[
            ChoiceDTO(
                "121",
                "????????????",
                False
            ),
            ChoiceDTO(
                "122",
                "????????????????????",
                True
            )
        ]

        questions: List[QuestionDTO] = [
            QuestionDTO(
                "1-1",
                "?? ?????????? ???????????? ???????????????????? ???????????????????????????",
                choices1
            ),
            QuestionDTO(
                "1-2",
                "?????? ?????????????????",
                choices2
            )
        ]

        self.quiz_dto = QuizDTO(
            "1",
            "????????????????????????????",
            questions
        )

    def test_right_answers_quiz_pass_result(self):
        answers: List[AnswerDTO] = [
            AnswerDTO(
                "1-1",
                ["111", "113"]
            ),
            AnswerDTO(
                "1-2",
                ["122"]
            )
        ]

        answers_dto = AnswersDTO(
            "1",
            answers
        )

        quiz_result_service = QuizResultService(
            self.quiz_dto,
            answers_dto
        )

        self.assertEqual(quiz_result_service.get_result(), 1.00)

    def test_only_one_right_answer_quiz_fail_result(self):
        answers: List[AnswerDTO] = [
            AnswerDTO(
                "1-1",
                ["111", "112"]
            ),
            AnswerDTO(
                "1-2",
                ["122"]
            )
        ]

        answers_dto = AnswersDTO(
            "1",
            answers
        )

        quiz_result_service = QuizResultService(
            self.quiz_dto,
            answers_dto
        )

        self.assertEqual(quiz_result_service.get_result(), 0.50)
    
    def test_no_right_answers_quiz_fail_result(self):
        answers: List[AnswerDTO] = [
            AnswerDTO(
                "1-1",
                ["111", "112"]
            ),
            AnswerDTO(
                "1-2",
                ["121"]
            )
        ]

        answers_dto = AnswersDTO(
            "1",
            answers
        )

        quiz_result_service = QuizResultService(
            self.quiz_dto,
            answers_dto
        )

        self.assertEqual(quiz_result_service.get_result(), 0.0)
