from .AddressBook import AddressBook


class AddressBookIterator:

    def __init__(self, address_book: AddressBook):
        self._records = list(address_book.data.values())
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._records):
            record = self._records[self._index]
            self._index += 1
            return record
        raise StopIteration
