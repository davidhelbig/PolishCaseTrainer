import unicodedata
from abc import ABCMeta, abstractmethod

from ..word.word import Word, Adjective, CaseNotSupported


class Question:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_question_text(self):
        pass

    @abstractmethod
    def get_question_options(self):
        pass

    @abstractmethod
    def evaluate(self, answer):
        pass

    @abstractmethod
    def get_correct_answer(self):
        pass


class NounCaseQuestion(Question):

    def __init__(self, noun, adjective, number, case):
        if not isinstance(noun, Word):
            raise TypeError("noun must be a Word object")
        if not isinstance(adjective, Adjective):
            raise TypeError("adjective must be a Ajective object")
        if number == "singular" and case == "nominative":
            raise CaseNotSupported(number, case)
        # May throw GenderNotSupported Exception
        adjective.set_gender(noun.get_gender())
        if not noun.supports(number, case) or not adjective.supports(number, case):
            raise CaseNotSupported(number, case)
        self._noun = noun
        self._adjective = adjective
        self._number = number
        self._case = case

    def get_question_elements(self):
        return {
            'noun_base_form': self._noun.get_basic_form(),
            'noun_gender': self._noun.get_gender(),
            'adj_base_form': self._adjective.get_basic_form(),
            'target_number': self._number,
            'target_case': self._case
        }

    def get_question_text(self):
        question_elements = self.get_question_elements()
        print(question_elements)
        return u"Noun: {} ({})\nAdjective: {}\nDecline for {} {}\n".format(
            question_elements['noun_base_form'],
            question_elements['noun_gender'],
            question_elements['adj_base_form'],
            question_elements['target_number'],
            question_elements['target_case']
        )

    def get_question_options(self):
        """
        Returning None signifies that this is not muliple choice.
        Because of this, the terminal service will give a standard text prompt.
        """
        return None

    def evaluate(self, answer):
        correct_forms = self.get_correct_answer()
        return unicodedata.normalize('NFC', answer) \
            == unicodedata.normalize('NFC', correct_forms)

    def get_correct_answer_elements(self):
        noun_form = self._noun.get_case_form(self._number, self._case)
        adjective_form = self._adjective.get_case_form(
            self._number, self._case)

        return {'noun_correct': noun_form, 'adj_correct': adjective_form}

    def get_correct_answer_text(self):
        answer_elements = self.get_correct_answer_elements()
        return u"{} {}".format(answer_elements['noun_correct'], answer_elements['adj_correct'])
