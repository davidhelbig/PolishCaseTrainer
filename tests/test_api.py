import api
from falcon import HTTP_200, HTTP_404, HTTP_400
import hug
import json

from polish_case_trainer.word.word_repository import WordRepository

def test_basic_function():
    response = hug.test.get(api, "/questions", query_string="numbers=plural&cases=genitive&num=5")
    assert response.data is not None

def test_numbers():
    response = hug.test.get(api, "/questions", query_string="numbers=plural&cases=genitive&num=5")
    assert all(question['question_elements']['target_number'] == "plural" for question in response.data)

def test_repeat_query_argument():
    response = hug.test.get(api, "/questions", query_string="numbers=plural&numbers=plural&cases=genitive")
    assert response.status == HTTP_200

def test_question_number():
    response = hug.test.get(api, "/questions", query_string="numbers=plural&cases=genitive&num=5")
    assert response.status == HTTP_200
    assert len(response.data) == 5

def test_question_number_negative():
    response = hug.test.get(api, "/questions", query_string="numbers=plural&cases=genitive&num=-5")
    assert response.status == HTTP_400