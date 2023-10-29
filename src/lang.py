from enum import Enum


class SelectLang(Enum):
    """
    Возвращает язык в виде строки
    """
    EN = 0
    RU = 1

    def __str__(self) -> str:
        return self.name
