from dataclasses import dataclass


# alt  + click lbm
@dataclass                       # функция декоратор позволяющий хранить в классе данные с определённым типом
class Person:
    full_name: str = None
    first_name: str = None
    last_name: str = None
    middle_name: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    mobile: str = None

# в датаклассах необходимо СТРОГО прописывать тип данных для свойств (данных) класса


@dataclass
class Color:
    color_name: list = None


@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None

