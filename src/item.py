import os
from csv import DictReader
from typing import Union


class InstantiateCSVError(Exception):
    """Класс исключения при повреждении файла"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл повреждён.'

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Добавляем экземпляр класса в список
        # Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """
        Предоставляет доступ на получение
        значения атрибута '__name' (геттер)
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Предоставляет доступ на изменение
        значения атрибута '__name' (сеттер)
        """
        if len(name) > 10:
            # print('Длина наименования товара превышает 10 символов.')
            name = name[:10]
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls, file_path: str = 'src/item.csv') -> str:
        """
        Получение данных из файла .csv.
        Создание на основе полученных данных экземпляров класса.
        Добавление экземпляров класса в список объектов класса.
        """
        path = os.path.join(os.path.dirname(__file__), '..', file_path)
        # "Обнуляем" список экземпляров класса
        cls.all = []
        # Проверяем наличие файла .csv
        try:
            with open(path, mode='r', encoding='windows-1251', newline='') as csvfile:
                # Считываем данные из файла в словарь.
                reader = DictReader(csvfile)
                # Перебираем полученные данные,
                # присваивая значения соответствующим переменным.
                # Проверяем наличие необходимых заголовков колонок.
                if reader.fieldnames == ['name', 'price', 'quantity']:
                    for row in reader:
                        # Проверяем наличие данных в колонках.
                        if not (row['name'] and row['price'] and row['quantity']) is None:
                            name = row['name']
                            price = cls.string_to_number(row['price'], 'Стоимость')
                            quantity = cls.string_to_number(row['quantity'], 'Количество')
                            # Если стоимость или количество не равны 0,
                            # то создаём новый экземпляр класса
                            if price != 0 and quantity != 0:
                                item = cls(name, price, quantity)
                            # Добавляем объект в список,
                            # если он не содержит эквивалентного ему объекта.
                            if item not in cls.all:
                                cls.all.append(item)
                        else:
                            raise InstantiateCSVError(f'Файл {cls.file_name(file_path)} повреждён.')
                else:
                    raise InstantiateCSVError(f'Файл {cls.file_name(file_path)} повреждён.')
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {cls.file_name(file_path)}.')

    @staticmethod
    def file_name(path):
        """
        Получение имени файла из полного имени, включающего путь к файлу
        """
        if '/' in path:
            file = path.split('/')[-1]
        else:
            indexes = [i for i, c in enumerate(path) if c == '\\']
            file = path[indexes[-1] + 1:]
        return file

    def __eq__(self, other):
        # сравнение двух экземпляров класса
        if isinstance(other, Item):
            return (self.name == other.name and
                    self.price == other.price and
                    self.quantity == other.quantity)
        # иначе возвращаем NotImplemented
        # return NotImplemented

    @staticmethod
    def string_to_number(str_num: str, str_row: str = 'Количество') -> Union[int, float]:
        """
        Возвращает целое или вещественное число из числа-строки.
        """
        try:
            # Если передана строка с целым числом или вещественным
            # с нулевой дробной частью, то возвращаем целое число.
            # Иначе возвращаем вещественное,
            # так как стоимость товара может быть float.
            num = float(str_num)
            if int(num % int(num)) == 0 and str_row == 'Количество':
                num = int(num)
            else:
                num = round(num, 2)
            return num
        except ValueError:
            num = 0
            # if str_row == 'Стоимость':
            #     print(f'Не корректная стоимость. {str_row} = 0')
            # else:
            #     print(f'Не корректное количество. {str_row} = 0')
            return num

    def __add__(self, other):
        """
        Сложение количества товаров класса Item и дочерних подклассов
        """
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
