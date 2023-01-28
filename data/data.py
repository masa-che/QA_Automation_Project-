from dataclasses import dataclass


@dataclass                       # функция декоратор позволяющий хранить в классе данные с определённым типом
class Person:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None

# в датаклассах необходимо СТРОГО прописывать тип данных для свойств (данных) класса