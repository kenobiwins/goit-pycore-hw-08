from typing import Tuple

from address_book import AddressBook
from decorators import command_error_handler
from enums import Color, Command
from handlers import (
    add_birthday,
    add_contact,
    change_birthday,
    change_contact,
    get_upcoming_birthdays,
    show_all,
    show_birthday,
    show_help,
    show_phone,
)


def parse_input(user_input: str) -> Tuple[str, list[str]]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@command_error_handler
def parse_command(command: str) -> Command:
    return Command(command)


def main() -> None:
    print(f"{Color.TITLE.value}Welcome to the assistant bot!")
    book = AddressBook()

    try:
        while True:
            user_input = (
                input(f"{Color.DEFAULT.value}Enter a command: ").strip().lower()
            )
            command, *args = parse_input(user_input)

            parsed_command = parse_command(command)

            if parsed_command is None:
                continue

            match parsed_command:
                case Command.EXIT | Command.CLOSE:
                    book.serialize_data()
                    print(f"{Color.TITLE.value}Good bye!")
                    break
                case Command.HELLO:
                    print(f"{Color.TITLE.value}How can I help you?")
                case Command.ADD:
                    print(add_contact(args, book))
                case Command.CHANGE:
                    print(change_contact(args, book))
                case Command.PHONE:
                    print(show_phone(args, book))
                case Command.ALL:
                    print(show_all(book))
                case Command.HELP:
                    print(show_help())
                case Command.ADD_BIRTHDAY:
                    print(add_birthday(args, book))
                case Command.SHOW_BIRTHDAY:
                    print(show_birthday(args, book))
                case Command.BIRTHDAYS:
                    print(get_upcoming_birthdays(book))
                case Command.CHANGE_BIRTHDAY:
                    print(change_birthday(args, book))
                case _:
                    print(f"{Color.ERROR.value}Error: Invalid command.")
    except Exception as e:
        print(f"{Color.ERROR.value}Exeption: {e}")


if __name__ == "__main__":
    main()
