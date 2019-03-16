from dataclasses import dataclass
from typing import Any


@dataclass
class FactRow:
    value: Any
    name: str
    question: str


@dataclass
class FactModel:
    name: FactRow
    gender: FactRow
    high: FactRow
    hair: FactRow
    humor: FactRow
    eyes: FactRow
    style: FactRow
    age: FactRow

    def __init__(self, name=None, gender=None, high=None, hair=None, humor=None, eyes=None, style=None, age=None):
        self.name = FactRow(name, 'Имя', 'Введите имя: ')
        self.gender = FactRow(gender, 'Пол', 'Мужчина или женщина? (м/ж): ')
        self.high = FactRow(high, 'Высокий', 'Этот человек высокий? (да/нет): ')
        self.hair = FactRow(hair, 'Цвет волос', 'Какой цвет волос? : ')
        self.humor = FactRow(humor, 'Чувство юмора', 'Хорошее чувство юмора? (да/нет): ')
        self.eyes = FactRow(eyes, 'Узкие глаза', 'Глаза зауженны? (да/нет): ')
        self.style = FactRow(style, 'Классический стиль', 'Любит классический стиль? (да/нет): ')
        self.age = FactRow(age, 'Возраст', 'Какой возраст? : ')

    def __str__(self):
        values = list()
        for k, v in self.__dict__.items():
            if isinstance(v.value, bool):
                values.append('да' if v.value else 'нет')
            else:
                values.append(str(v.value))
        return ','.join(values)

    def __repr__(self):
        out = ''
        for v in list(self.__dict__.values()):
            if isinstance(v.value, bool):
                out += v.name + ': ' + ('Да' if v.value else 'Нет') + '\n'
            else:
                out += v.name + ': ' + str(v.value).capitalize() + '\n'
        return out
