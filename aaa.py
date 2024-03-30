from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
def parse():
    url = 'https://auto.drom.ru/'
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
    block = soup.findAll('a', class_='css-4zflqt e1huvdhj1') # находим  контейнер с нужным классом
    for car in block:
        name=car.find('div', class_='css-16kqa8y e3f4v4l2').find('span')
        name_car = name.text # записываем в переменную содержание тега
        print(name_car)
        price=car.find('span', class_="css-46itwz e162wx9x0")
        price_car=price.text
        print(price_car)
        with open('output.txt', 'a', encoding='utf-8') as f:
            f.write(name.text)
            f.write('\n')
            f.write(price.text)
            f.write('\n')
parse()

