from address_book import AddressBook

from .Command import Command


class AddBirthdayCommand(Command):

    def __init__(self, address_book: AddressBook, name: str, birthday:None | str=None) -> None:
        self.address_book = address_book
        self.name = name
        self.birthday = birthday

    def execute(self) -> None:
        record = self.address_book.find(self.name)
        record.add_birthday(self.birthday)
