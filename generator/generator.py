from data.data import Person, Color, Date
from faker import Faker
import random

# Faker — это пакет Python с открытым исходным кодом, используемый для создания поддельного набора данных
# для тестирования приложений
faker_ru = Faker('ru_RU')     # создаём экземпляр класса с синтаксисом и языком для малых и заглавных букв
faker_en = Faker('en_US')
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
    path = rf'c:\Users\Maxim\PycharmProjects\QA_Pet_Automation_Project\filetest{random.randint(0, 101)}.txt'
    file = open(path, 'w+')                         # функция open файл (path путь к файлу ,'w+' открытие файла с редак)
    file.write(f'Hello amigo,do you remember me?')  # записываем в файл данные
    file.close()                                    # закрываем файл
    return file.name, path                          # возвращаем имя файла и его путь где он лежит (для проверок)


def generated_subject():
    sub_list = ['Hindi', 'English', 'Maths', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'Commerce',
                'Accounting', 'Economics', 'Arts', 'Social Studies', 'History', 'Civics']
    subject = random.choice(sub_list)
    return subject


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time='18:00'
    )


# практическое задание вкладка "Widgets"-->"Select Menu"
def generated_select_value():
    select_value = ["Group 1, option 1", "Group 1, option 2", "Group 2, option 1", "Group 2, option 2", "A root option",
                    "Another root option"]
    value = random.choice(select_value)
    return value


def generated_select_one():
    select_value = ["Dr.", "Mr.", "Mrs.", "Ms.", "Prof.", "Other"]
    value_one = random.choice(select_value)
    return value_one


def generated_colors_old_select():
    select_color = ["Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    color_old = random.choice(select_color)
    return color_old


def generated_color_multiselect():
    yield Color(
        color_name=["Green", "Blue", "Black", "Red"]
    )

