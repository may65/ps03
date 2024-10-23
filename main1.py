from bs4 import BeautifulSoup
import requests

# URL страницы
url = "http://quotes.toscrape.com/"
response = requests.get(url)
html = response.text

# Создаем объект BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Находим все элементы с классом quote
quotes = soup.find_all("div", class_="quote")

# Проходим по каждому элементу и извлекаем данные
for i, quote in enumerate(quotes, start=1):
    # Извлекаем текст цитаты
    text = quote.find("span", class_="text").text
    # Извлекаем автора
    author = quote.find("small", class_="author").text
    # Извлекаем теги
    tags = [tag.text for tag in quote.find_all("a", class_="tag")]

    # Выводим результаты
    print(f"Цитата номер - {i}")
    print(f"Цитата: {text}")
    print(f"Автор: {author}")
    print(f"Теги: {', '.join(tags)}\n")