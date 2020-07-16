from enum import Enum


class Category(Enum):
    """ 定数コード """
    development_language = 1


class DevelopmentLanguage(Enum):
    """ 開発言語 """
    PYTHON = 1
    TYPESCRIPT = 2
    C_SHARP = 3
