"""Здесь надо написать тесты с использованием pytest для модуля item."""
import os
from csv import DictReader

import pytest
from typing import Union

from src.item import Item


@pytest.mark.parametrize('name, price, quantity, result', [
    ('Смартфон', 10000, 20, 200000),
    ('Ноутбук', 20000, 5, 100000),
    ('Фотобумага', 600.25, 30, 18007.50),
    ('Флеш-накопитель', 345.15, 63, 21744.45),
])
def test_calculate_total_price(name: str, price: float, quantity: int, result: float) -> None:
    """
    Тестирование метода класса calculate_total_price(),
    рассчитывающего общую стоимость товаров в магазине.
    :param name: Наименование товара, str.
    :param price: Стоимость товара, float.
    :param quantity: Количество товара, int.
    :param result: Ожидаемый результат, int, float.
    :return: Ошибки, если они имеются.
    """
    # Создаём экземпляр класса
    item = Item(name, price, quantity)

    # Тестируем экземпляр класса Operation
    assert round(item.calculate_total_price(), 2) == result


@pytest.mark.parametrize('name, price, quantity, pay_r, result', [
    ('Смартфон', 10000, 20, 0.8, 8000),
    ('Ноутбук', 20000, 5, 0.9, 18000),
    ('Фотобумага', 600.25, 30, 0.85, 510.21),
    ('Флеш-накопитель', 345.15, 63, 0.97, 334.80),
])
def test_apply_discount(name: str, price: float, quantity: int, pay_r: float, result: float) -> None:
    """
    Тестирование метода класса calculate_total_price(),
    рассчитывающего общую стоимость товаров в магазине.
    :param name: Наименование товара, str.
    :param price: Стоимость товара, float.
    :param quantity: Количество товара, int.
    :param pay_r: Новый уровень цены, float.
    :param result: Ожидаемый результат, int, float.
    :return: Ошибки, если они имеются.
    """
    # Создаём экземпляр класса
    item = Item(name, price, quantity)

    # устанавливаем новый уровень цен
    Item.pay_rate = pay_r

    # применяем скидку
    item.apply_discount()

    # Тестируем экземпляр класса Operation
    assert round(item.price, 2) == result


@pytest.mark.parametrize('name, price, quantity', [
    ('Смартфон', 10000, 20),
    ('Ноутбук', 20000, 5),
    ('Фотобумага', 600.25, 30),
    ('Флеш-накопитель', 345.15, 63),
])
def test_apply_discount_1(name: str, price: float, quantity: int) -> None:
    """
    Тестирование функции apply_discount,
    не возвращающей значение.
    :param name: Наименование товара, str.
    :param price: Стоимость товара, float.
    :param quantity: Количество товара, int.
    :return: Ошибки, если они имеются.
    """
    # Создаём экземпляр класса
    item = Item(name, price, quantity)

    # Тестируем экземпляр класса Operation
    assert item.apply_discount() is None


@pytest.mark.parametrize('name, price, quantity,  result', [
    ('Смартфон', 10000, 20, 0),
    ('Ноутбук', 20000, 5, 0),
    ('Фотобумага', 600.25, 30, 0),
    ('Флеш-накопитель', 345.15, 63, 0),
])
def test_item_all(name: str, price: float, quantity: int, result: float) -> None:
    """
    Тестирование количества созданных объектов.
    :param name: Наименование товара, str.
    :param price: Стоимость товара, float.
    :param quantity: Количество товара, int.
    :param result: Ожидаемый результат, int, float.
    :return: Ошибки, если они имеются.
    """
    # Создаём экземпляр класса
    item = Item(name, price, quantity)

    # Тестируем экземпляр класса Operation
    assert len(item.all) == result


def test_name() -> None:
    """Тестирование сеттера"""
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'


def test_instantiate_from_csv() -> None:
    """Тестирование функции"""
    path = os.path.join(os.path.dirname(__file__), 'items.csv')
    Item.instantiate_from_csv(path)  # создание объектов из данных файла
    # Количество в файле корректных записей с данными по товарам
    names = []
    for obj_name in Item.all:
        names.append(obj_name.name)
    print(names)
    assert len(Item.all) == 5

    # Первый экземпляр класса с наименованием "Смартфон"
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    # В файле 8 записей с данными по товарам
    csv_list = []
    with open(path, mode='r') as csvfile:
        # Считываем данные из файла в список.
        reader = DictReader(csvfile)
        for row in reader:
            csv_l = [row['name'], row['price'], row['quantity']]
            csv_list.append(csv_l)
    assert len(csv_list) == 8


@pytest.mark.parametrize('num, name_row, result', [
    ('5', 'Количество', 5),
    ('5.0', 'Количество', 5),
    ('5.5', 'Количество', 5),
    ('1025.5', 'Стоимость', 1025.5),
    ('1025.0', 'Стоимость', 1025),
    ('Ошибка', 'Стоимость', 0),
    ('Ошибка', 'Количество', 0)
])
def test_string_to_number(num: str, name_row: str, result: Union[int, str]) -> None:
    """
    Тестирование функции преобразования целого или вещественного числа из числа-строки
    """
    assert Item.string_to_number(num, name_row) == result


def test_repr_str():
    """
    Тесты __repr__ и __str__
    """
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
