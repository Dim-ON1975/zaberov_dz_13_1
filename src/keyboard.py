from src.item import Item
from src.lang import SelectLang


class Language:
    """
    Миксин изменения языка клавиатуры
    """

    def __init__(self) -> None:
        self.__language = SelectLang.EN

    def change_lang(self) -> None:
        if self.__language == SelectLang.EN:
            self.__language = SelectLang.RU
        else:
            self.__language = SelectLang.EN

    @property
    def language(self):
        return self.__language


class Keyboard(Item, Language):
    """
    Класс для товара "Клавиатура"
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name
