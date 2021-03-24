# class representing vocabulary card
from src.enums.language import Language
from src.enums.status import Status


class VocabularyCard(object):

    def __init__(self, name, translations, language):
        self.name = name
        self.translations = translations
        self.language = language
        self.status = Status.NEW

    def __repr__(self):
        return "<Vocabulary card> Name: " + self.name + ", Translations: " + str(self.translations) \
               + ", Language: " + self.language + ", Status: " + str(self.status)
