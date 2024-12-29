from address_book import AddressBook

from .Command import Command


class DeleteRecordCommand(Command):

    def __init__(self, address_book: AddressBook, name: str) -> None:
        self.address_book = address_book
        self.name = name

    def execute(self) -> None:
        self.address_book.delete(self.name)
