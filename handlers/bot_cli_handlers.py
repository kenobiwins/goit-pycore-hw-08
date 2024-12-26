from address_book import AddressBook, AddressBookIterator
from commands import AddBirthdayCommand, AddRecordCommand, FindRecordCommand
from decorators import handle_input_error
from enums import COMMAND_DESCRIPTIONS, Color
from models import Record


@handle_input_error
def add_contact(args: list[str], book) -> str:
    if len(args) < 2:
        raise IndexError

    name, phone, *_ = args
    existing_record = book.find(name)

    if existing_record is None:
        record = Record(name)
        record.add_phone(phone)
        add_command = AddRecordCommand(book, record)
        add_command.execute()
        return f"{Color.SUCCESS.value}Contact added."
    else:
        existing_record.add_phone(phone)
        return f"{Color.SUCCESS.value}Phone added to existing contact."


@handle_input_error
def change_contact(args: list[str], book) -> str:
    if len(args) < 2:
        raise IndexError
    name, old_phone, new_phone, *_ = args
    existing_record = book.find(name)
    if existing_record is None:
        return f"{Color.ERROR.value}Contact not found."
    else:
        existing_record.edit_phone(old_phone, new_phone)
        return f"{Color.SUCCESS.value}Phone changed."


@handle_input_error
def show_phone(args: list[str], book: AddressBook) -> str:
    result = []

    (name,) = args
    find_command = FindRecordCommand(book, name)
    record = find_command.execute()

    if record is None:
        return f"{Color.ERROR.value}Contact not found."

    phones = record.show_phones()  
    if phones:
        result.append(f"{Color.INFO.value}Phone Numbers:")
        for phone in phones:
            result.append(f"📱 {phone}")
    else:
        result.append(f"{Color.WARNING.value}No phone numbers available.")

    return "\n".join(result)

@handle_input_error
def show_all(book: AddressBook) -> str:
    result = [f"{Color.HIGHLIGHT.value}All Contacts:"]

    if not book.data:
        return f"{Color.INFO.value}No contacts available."

    iterator = AddressBookIterator(book)
    for record in iterator:
        result.append(f"{Color.INFO.value}{record}")

    return "\n".join(result)


@handle_input_error
def show_help() -> str:
    result = [f"{Color.HIGHLIGHT.value}Available Commands:"]
    for command, description in COMMAND_DESCRIPTIONS.items():
        result.append(f"{Color.DEFAULT.value}{command.value}: {description}")
    return "\n".join(result)


@handle_input_error
def add_birthday(args, book: AddressBook)   -> str:
    if len(args) < 2:
        raise IndexError
    name, birthday, *_ = args
    AddBirthdayCommand(book, name, birthday).execute()
    return f"{Color.SUCCESS.value}Birthday added."

@handle_input_error
def change_birthday(args, book: AddressBook) -> str:
    if len(args) < 2:
        raise IndexError
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        return f"{Color.ERROR.value}Contact not found."
    record.change_birthday(birthday)
    return f"{Color.SUCCESS.value}Birthday changed."

@handle_input_error
def show_birthday(args, book: AddressBook)  -> str:
    name = args[0]
    record = book.find(name)
    return f"{Color.INFO.value}{name}'s birthday: {record.birthday}"


@handle_input_error
def get_upcoming_birthdays(book: AddressBook):
    birthdays = book.get_upcoming_birthdays()

    if not birthdays:
        return f"{Color.INFO.value}No upcoming birthdays found."

    result = f"{Color.HIGHLIGHT.value}Upcoming Birthdays:\n"
    for birthday in birthdays:
        if birthday["congratulation_date"]: 
            result += f"{Color.INFO.value}🎂 {birthday['name']}: {birthday['congratulation_date']}\n"
        else:  
            result += (
                f"{Color.INFO.value}🎂 {birthday['name']}: No birthday date available\n"
            )
    return result.strip()
