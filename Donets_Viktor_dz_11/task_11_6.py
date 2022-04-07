# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий
# склад. А также класс «Оргтехника», который будет базовым для
# классов-наследников. Эти классы — конкретные типы оргтехники (принтер,
# сканер, ксерокс). В базовом классе определите параметры, общие для
# приведённых типов. В классах-наследниках реализуйте параметры, уникальные
# для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработайте методы, которые отвечают
# за приём оргтехники на склад и передачу в определённое подразделение
# компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру
# (например, словарь).

# Продолжить работу над вторым заданием. Реализуйте механизм валидации
# вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум
# возможностей, изученных на уроках по ООП.


# Склад
class Warehouse:
    # name - название склада, number_of_cells - количество ячееек на складе
    def __init__(self, name, number_of_cells):
        self.name = name
        self.number_of_cells = number_of_cells
        self.warehouse = {}

    def __str__(self):
        return f'{self.name}: {self.warehouse}'

    @staticmethod
    def validator(numeric):
        if not numeric.isdigit():
            while not numeric.isdigit():
                print(f'{numeric} не является числом!')
                numeric = input('Введите число повторно: ')
        return int(numeric)

    # Приход на склад equipment - полное название товара,
    # number - его количество
    def take_to_warehouse(self, equipment, number):
        valid_take = Warehouse.validator(number)
        if valid_take and equipment not in self.warehouse:
            self.warehouse[equipment] = valid_take
            print(f'На {self.name}  получен * {equipment} * '
                  f'в количестве {valid_take}')
        elif valid_take and equipment in self.warehouse:
            self.warehouse[equipment] += valid_take
            print(f'На {self.name}  получен * {equipment} * '
                  f'в количестве {valid_take}')

    # Перемещение со склада equipment - полное название товара,
    # number - его количество
    def give_to_warehouse(self, equipment, other_warehouse, number):
        valid_give = Warehouse.validator(number)
        if valid_give and equipment not in self.warehouse:
            print(f'Attention!!! **** Такого товара на {self.name} нет ****')
        elif valid_give and self.warehouse[equipment] - valid_give < 0:
            print(f'Attention!!! **** На {self.name} такого количества товара'
                  f' * {equipment} * в количестве {valid_give} шт. нет **** '
                  f'Остаток: {self.warehouse[equipment]}')
        elif valid_give and equipment in self.warehouse:
            self.warehouse[equipment] -= valid_give
            print(f'С {self.name} перемещен на {other_warehouse.name}'
                  f' * {equipment} * в количестве {valid_give}')
            other_warehouse.take_to_warehouse(equipment, str(valid_give))


# Оргтехника. producer-производитель, network-сетевой
class OfficeEquipment:
    def __init__(self, producer, model, serial_number, network=False):
        self.producer = producer
        self.model = model
        self.serial_number = serial_number
        self.network = network


# Принтеры. color - цветной или черно-белый
class Printer(OfficeEquipment):
    def __init__(self, producer, model, serial_number,
                 type_printer, network=False, color='Черно-белый'):
        super().__init__(producer, model, serial_number, network)
        # типы принтеров: лазерный, струйный, светодиодный, матричный
        self.type_printer = type_printer
        self.color = color

    def __str__(self):
        return f'Принтер: Производитель-{self.producer}, модель-{self.model},' \
               f' серийный номер-{self.serial_number},' \
               f' тип принтера-{self.type_printer}, сетевой-{self.network},' \
               f' цветность-{self.color}'

    def __repr__(self):
        return '*'.join(['printer', self.producer, self.model])


# Сканеры. wireless - проводной или безпроводной
class Scanner(OfficeEquipment):
    def __init__(self, producer, model, serial_number,
                 type_scanner, network=False, wireless=False):
        super().__init__(producer, model, serial_number, network)
        # типы сканеров: документальный, планшетный, ручной, широкоформатный
        self.type_scanner = type_scanner
        self.wireless = wireless

    def __str__(self):
        return f'Сканер: Производитель-{self.producer}, модель-{self.model},' \
               f' серийный номер-{self.serial_number},' \
               f' тип сканера-{self.type_scanner}, ' \
               f' сетевой-{self.network}, беспроводной-{self.wireless}'

    def __repr__(self):
        return '*'.join(['scaner', self.producer, self.model])


# Ксероксы
class Xerox(Printer, OfficeEquipment):
    def __init__(self, producer, model, serial_number, type_xerox,
                 wireless=False, network=False, color='Черно-белый'):
        super().__init__(producer, model, serial_number, wireless, network,
                         color)
        # типы ксероксов: отдельный, МФУ, портативный, вендинговый
        self.type_xerox = type_xerox
        self.wireless = wireless

    def __str__(self):
        return f'Ксерокс: Производитель-{self.producer}, модель-{self.model},' \
               f' серийный номер-{self.serial_number},' \
               f' тип ксерокса-{self.type_xerox}, сетевой-{self.network}, ' \
               f' беспроводной-{self.wireless}, цветность-{self.color}'

    def __repr__(self):
        return '*'.join(['xerox', self.producer, self.model])


warehouse_1 = Warehouse('Store warehouse', 100)
warehouse_2 = Warehouse('Base warehouse', 800)
print(warehouse_1)
print(warehouse_2)
printer_1 = Printer('HP', 'LJ-1010', 'Lj125487hp', 'Лазерный')
print(printer_1)
scanner_1 = Scanner('Canon', 'LiDE 400', 'Ca1254875sc', 'Планшетный', True)
print(scanner_1)
xerox_1 = Xerox('Pantum', 'M6500W', 'Pa125d55xe', 'МФУ', True, True, 'Цветной')
print(xerox_1)
warehouse_2.take_to_warehouse(printer_1, input('Введите количество техники: '))
warehouse_2.take_to_warehouse(printer_1, input('Введите количество техники: '))
warehouse_2.take_to_warehouse(scanner_1, input('Введите количество техники: '))
warehouse_2.take_to_warehouse(scanner_1, input('Введите количество техники: '))
warehouse_1.take_to_warehouse(scanner_1, input('Введите количество техники: '))
print(warehouse_1)
print(warehouse_2)
warehouse_1.give_to_warehouse(xerox_1, warehouse_1, input(
    'Введите количество техники для перемещения: '))
warehouse_2.give_to_warehouse(scanner_1, warehouse_1, input(
    'Введите количество техники для перемещения: '))
warehouse_2.give_to_warehouse(scanner_1, warehouse_1, input(
    'Введите количество техники для перемещения: '))
print(warehouse_1)
print(warehouse_2)
