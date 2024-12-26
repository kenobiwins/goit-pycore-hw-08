from address_book import AddressBook
from models import Record

from .Command import Command


class AddRecordCommand(Command):

    def __init__(self, address_book: AddressBook, record: Record) -> None:
        self.address_book = address_book
        self.record = record

    def execute(self) -> None:
        self.address_book.add_record(self.record)
