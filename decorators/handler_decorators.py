from functools import wraps
from typing import Any, Callable

from enums import Color


def handle_input_error(func: Callable[..., str]) -> Callable[..., str]:
    @wraps(func)
    def handler(*args: Any, **kwargs: Any) -> str:
        try:

            return func(*args, **kwargs)
        except KeyError:
            return f"{Color.ERROR.value}Error: Contact not found."
        except ValueError as e:
            return f"{Color.ERROR.value}Error: {e}"
        except IndexError:
            return f"{Color.ERROR.value}Error: Not enough arguments provided. Two arguments (name and phone) are required."

    return handler

def command_error_handler(func: Callable[[str, Any], Any]) -> Callable[[str, Any], Any]:
    @wraps(func)
    def handler(command: str, *args: Any, **kwargs: Any) -> Any:
        try:
            return func(command, *args, **kwargs)
        except ValueError:
            print(
                f"{Color.ERROR.value}Error: Invalid command. Type 'help' to see available commands for the CLI."
            )
            return None

    return handler
