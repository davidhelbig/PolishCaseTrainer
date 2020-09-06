# -*- coding: utf-8 -*-
from unittest.mock import Mock

import pytest

from polish_case_trainer.question.question_bag import QuestionBag, NounCaseQuestionBag
from polish_case_trainer.word.word_bag import WordBag


def test_cannot_instantiate_question_bag_abstract_object():
    with pytest.raises(TypeError):
        question_bag = QuestionBag()

def test_noun_case_question_bag_instantiation_fails_without_arguments():
    with pytest.raises(TypeError):
        question_bag = NounCaseQuestionBag()


def test_noun_case_question_bag_instantiation_fails_if_first_argument_isnt_word_bag_object():
    noun_bag = Mock()
    with pytest.raises(TypeError):
        question_bag = NounCaseQuestionBag(noun_bag, None, None, None)


def test_noun_case_question_bag_instantiation_fails_if_second_argument_isnt_adjective_object():
    noun_bag = Mock(spec=WordBag)
    adjective_bag = Mock()
    with pytest.raises(TypeError):
        question_bag = NounCaseQuestionBag(noun_bag, adjective_bag, None, None)


def test_noun_case_question_bag_instantiation_fails_if_third_argument_isnt_list():
    noun_bag = Mock(spec=WordBag)
    adjective_bag = Mock(spec=WordBag)
    allowed_numbers = "invalid"
    with pytest.raises(TypeError):
        question_bag = NounCaseQuestionBag(
            noun_bag, adjective_bag, allowed_numbers, None)


def test_noun_case_question_bag_instantiation_fails_if_fourth_argument_isnt_list():
    noun_bag = Mock(spec=WordBag)
    adjective_bag = Mock(spec=WordBag)
    allowed_numbers = []
    allowed_cases = "invalid"
    with pytest.raises(TypeError):
        question_bag = NounCaseQuestionBag(
            noun_bag, adjective_bag, allowed_numbers, allowed_cases)


def test_noun_case_question_bag_instantiation_succeeds_with_valid_arguments():
    noun_bag = Mock(spec=WordBag)
    adjective_bag = Mock(spec=WordBag)
    allowed_numbers = []
    allowed_cases = []
    question_bag = NounCaseQuestionBag(
        noun_bag, adjective_bag, allowed_numbers, allowed_cases)
    assert isinstance(question_bag, QuestionBag) and isinstance(
        question_bag, NounCaseQuestionBag)

# Some more tests here would be good, after the coupling between NounCaseQuestionBag
# and NounCaseQuestion is removed.
