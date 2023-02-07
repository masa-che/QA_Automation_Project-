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
    )
# .seed() - модуль позволяющий гарантировать, что при дальнейших запусках тестов, в наши поля веб страницы TextBox,
# будут подставляться ОДИНАКОВЫЕ значения из генерируемых данных, соответствующие параметрам (name, email, address)
# для каждого поля.

