# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать методы
# экземпляров.

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name} {self.position}'

    def get_total_income(self):
        total_income = 0
        for key, item in self._income.items():
            total_income += item
        return f'Общий доход {round(total_income, 2)}'


position = Position('Viktor', 'Donets', 'manager',
                    {"wage": 150000.5, "bonus": 38080.12})
print(position.get_full_name())
print(position.get_total_income())
