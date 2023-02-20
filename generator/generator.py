from data.data import Person
from faker import Faker
import random

# Faker — это пакет Python с открытым исходным кодом, используемый для создания поддельного набора данных
# для тестирования приложений
faker_ru = Faker('ru_RU')     # создаём экземпляр класса с синтаксисом и языком для малых и заглавных букв
Faker.seed()


def generated_person():       # функция генератор (yield возвращает генератор для класса Person с его атрибутами)
    yield Person(
        full_name=faker_ru.last_name() + " " + faker_ru.first_name() + " " + faker_ru.middle_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(18, 64),
        department=faker_ru.job(),
        salary=random.randint(35000, 150000),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
    )
# .seed() - модуль позволяющий гарантировать, что при дальнейших запусках тестов, в поля веб страниц,
# будут подставляться ОДИНАКОВЫЕ значения из генерируемых данных, соответствующие параметрам (name, email, address)


def generated_file():                               # функция генератор создания файла, для теста upload system
    # r- "сырая строка" обход экранирования (чтобы не ругалось на бэкслеш) и f- для редактирования
    path = rf'c:\Users\Максим\PycharmProjects\QA_Automation_Project-\filetest{random.randint(0, 101)}.txt'
    file = open(path, 'w+')                         # функция open файл (path путь к файлу ,'w+' открытие файла с редак)
    file.write(f'Hello amigo,do you remember me?')  # записываем в файл данные
    file.close()                                    # закрываем файл
    return file.name, path                          # возвращаем имя файла и его путь где он лежит (для проверок)


def generated_subject():
    sub_list = ['Hindi', 'English', 'Maths', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'Commerce',
                'Accounting', 'Economics', 'Arts', 'Social Studies', 'History', 'Civics']
    subject = random.choice(sub_list)
    return subject
