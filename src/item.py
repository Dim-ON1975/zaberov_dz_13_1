from csv import DictReader
from typing import Union


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
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Добавляем экземпляр класса в список
        Item.all.append(self)

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
    def instantiate_from_csv(cls, path: str):
        """
        Получение данных из файла .csv.
        Создание на основе полученных данных экземпляров класса.
        Добавление экземпляров класса в список объектов класса.
        """
        # "Обнуляем" список экземпляров класса
        cls.all = []
        with open(path, mode='r') as csvfile:
            # Считываем данные из файла в словарь.
            reader = DictReader(csvfile)
            # Перебираем полученные данные,
            # присваивая значения соответствующим переменным
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'], 'Стоимость')
                quantity = cls.string_to_number(row['quantity'], 'Количество')
                # Если стоимость или количество не равны 0,
                # то создаём новый экземпляр класса
                if price != 0 and quantity != 0:
                    item = cls(name, price, quantity)
                if item not in cls.all:
                    cls.all.append(item)

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
