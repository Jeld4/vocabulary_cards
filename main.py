# Hello World!
# This is gonna be awesome vocabulary cards education app! :)
from src.vocabulary_card import VocabularyCard


def main():
    print("Start the application")
    lan = input("Which language? 1=ENG, 2=CZE, 3=SLK, 4=GER: ")
    name = input("Enter the name: ")
    trans = input("Enter the translations: ")
    translations = trans.split(" ")
    card = VocabularyCard(name, translations, lan)
    print(repr(card))


if __name__ == "__main__":
    main()
