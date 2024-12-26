from address_book import AddressBook

from .Command import Command


class FindRecordCommand(Command):

    def __init__(self, address_book: AddressBook, name:str) -> None:
        self.address_book = address_book
        self.name = name

    def execute(self)->None:
        return self.address_book.find(self.name)
