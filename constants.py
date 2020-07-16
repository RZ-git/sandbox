from enum import Enum


class Category(Enum):
    """ 定数コード """
    development_language = 1


class DevelopmentLanguage(Enum):
    """ 開発言語 """
    python = 1
    typescript = 2
    c_sharp = 3
