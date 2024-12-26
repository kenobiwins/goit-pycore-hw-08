from enum import Enum

from colorama import Fore


class Color(Enum):
    SUCCESS = Fore.GREEN
    ERROR = Fore.RED
    INFO = Fore.BLUE
    WARNING = Fore.YELLOW
    TITLE = Fore.MAGENTA
    HIGHLIGHT = Fore.CYAN
    DEFAULT = Fore.WHITE
