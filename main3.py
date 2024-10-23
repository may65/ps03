# Попробуем работать с другим сайтом — randomword.com
# Здесь постоянно выдаются рандомные слова, с которыми мы создадим мини - игру.

import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаем объект переводчика
translator = Translator()

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        # Перевод слова на русский
        russian_word = translator.translate(english_words, src='en', dest='ru').text
        # Перевод определения на русский
        russian_definition = translator.translate(word_definition, src='en', dest='ru').text
        return {
            "english_words": english_words,
            "word_definition": word_definition,
            "russian_word": russian_word,
            "russian_definition": russian_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")

# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word_en = word_dict.get("english_words")
        word_definition_en = word_dict.get("word_definition")
        word = word_dict.get("russian_word")
        word_definition = word_dict.get("russian_definition")
        # Начинаем игру
        print(f"English - {word_definition_en}:{word_en}")
        print(f"Русский - {word_definition}:{word}")
        user = input("Что это за слово? ")
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")
        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()