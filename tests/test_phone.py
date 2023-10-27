import pytest

from src.phone import Phone


@pytest.mark.parametrize('name, price, quantity, sim_card', [
    ('Смартфон_1', 10000, 20, 2),
    ('Смартфон_2', 20000, 30, 1)
])
def test_init(name: str, price: float, quantity: int, sim_card: int) -> None:
    """
    Тестирование инициализатора класса Phone.
    :param name: Наименование товара, str.
    :param price: Стоимость товара, float.
    :param quantity: Количество товара, int.
    :param sim_card: Количество сим-карт, int.
    :return: Ошибки, если они имеются.
    """
    # Создаём экземпляр класса
    phone1 = Phone(name, price, quantity, sim_card)

    assert phone1.name == name
    assert phone1.price == price
    assert phone1.quantity == quantity
    assert phone1.number_of_sim == sim_card

    with pytest.raises(ValueError) as exif:
        str(Phone('Смартфон_3', 20000, 30, 0))
    assert "Количество физических SIM-карт должно быть целым числом больше нуля." in str(exif.value)


def test_number_of_sim() -> None:
    """
    Тестирование сеттера и геттера класса Phone.
    """
    # Создаём экземпляр класса
    phone1 = Phone('Смартфон_1', 10000, 20, 2)
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1

    phone2 = Phone('Смартфон_2', 20000, 30, 3)
    phone2.number_of_sim = 2
    assert phone2.number_of_sim == 2

    with pytest.raises(ValueError) as exif:
        phone2.number_of_sim = 0
    assert "Количество физических SIM-карт должно быть целым числом больше нуля." in str(exif.value)


def test_repr_str():
    """
    Тесты __repr__ и __str__
    """
    phone1 = Phone('Смартфон_1', 10000, 20, 2)
    assert repr(phone1) == "Phone('Смартфон_1', 10000, 20, 2)"
    assert str(phone1) == 'Смартфон_1'
