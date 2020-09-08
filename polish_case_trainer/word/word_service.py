
class WordService:

    def __init__(self, word_repository, word_factory):
        self.word_repository = word_repository
        self.word_factory = word_factory

    def get_noun_list(self):
        nouns = []
        for obj in self.word_repository.retrieve_nouns():
            try:
                nouns.append(self.word_factory.create_noun_from_json_object(obj))
            except ValueError:
                continue
        return nouns

    def get_adjective_list(self):
        adjectives = []
        for obj in self.word_repository.retrieve_adjectives():
            try:
                adjectives.append(
                    self.word_factory.create_adjective_from_json_object(obj))
            except ValueError:
                continue
        return adjectives
