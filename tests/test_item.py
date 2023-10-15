"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.item import Item


@pytest.mark.parametrize('name, price, quantity, result', [
    ('Смартфон', 10000, 20, 200000),
    ('Ноутбук', 20000, 5, 100000),
    ('Фотобумага', 600.25, 30, 18007.50),
    ('Флеш-накопитель', 345.15, 63, 21744.45),
])
def test_calculate_total_price(name: str, price: float, quantity: int, result: float):
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
def test_apply_discount(name: str, price: float, quantity: int, pay_r: float, result: float):
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
def test_apply_discount_1(name: str, price: float, quantity: int):
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
    ('Смартфон', 10000, 20, 13),
    ('Ноутбук', 20000, 5, 14),
    ('Фотобумага', 600.25, 30, 15),
    ('Флеш-накопитель', 345.15, 63, 16),
])
def test_item_all(name: str, price: float, quantity: int, result: float):
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
    assert len(Item.all) == result
