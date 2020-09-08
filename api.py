from polish_case_trainer.word.word_repository import WordRepository
from polish_case_trainer.word.word_factory import WordFactory
from polish_case_trainer.word.word_service import WordService
from polish_case_trainer.word.word_bag import WordBag
from polish_case_trainer.question.question_bag import NounCaseQuestionBag

import hug

NUMBERS_AVAILABLE = ["singular", "plural"]
CASES_AVAILABLE = [
        "nominative", "genitive", "dative", "accusative",
        "instrumental", "locative", "vocative"
    ]

MAX_NUM = 50 # maximum number of questions that can be retrieved at once

class OneOrManyOf(hug.types.Multiple):

    def __init__(self, allowed_values):
        self.allowed_values = allowed_values

    def __call__(self, input_value):
        as_multiple = super().__call__(input_value)

        if not all(value in self.allowed_values for value in as_multiple):
            raise KeyError(
                "Invalid value passed. The accepted values are: ({0})".format("|".join(self.allowed_values))
            )
        return as_multiple

# initialize NounBag
word_service = WordService(WordRepository(), WordFactory())
noun_bag = WordBag(word_service.get_noun_list())
adjective_bag = WordBag(word_service.get_adjective_list())

# add the CORS middleware to the module API singleton
api = hug.API(__name__)
# if called with no arguments except the api, all origins ('*') will be allowed.
api.http.add_middleware(hug.middleware.CORSMiddleware(api, allow_credentials=False))

@hug.get("/questions", examples=['numbers=singular&cases=genitive&cases=dative'])
def get_question(
    numbers: OneOrManyOf(NUMBERS_AVAILABLE),
    cases: OneOrManyOf(CASES_AVAILABLE),
    num: hug.types.in_range(1, MAX_NUM + 1) = 10):
    """ When queried for one or multiple numbers and cases, this endpoint returns a random question. """

    questions = []

    bag = NounCaseQuestionBag(
        noun_bag,
        adjective_bag,
        numbers,
        cases)

    while len(questions) < num:
        question = bag.get_question()
        questions.append(
            {
                'question_elements': question.get_question_elements(),
                'answer_elements': question.get_correct_answer_elements()
            })

    return questions
    