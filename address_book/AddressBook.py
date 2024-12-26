from collections import UserDict
from pathlib import Path

from memento import Memento
from models import Record
from utils import BirthdayHelper, Serializer


class AddressBook(UserDict):
    __instance = None
    DATA_FILE = Path(__file__).parent / ".data" / "address_book.pkl"

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(AddressBook, cls).__new__(cls, *args, **kwargs)
            cls.__instance._initialize_data()
        return cls.__instance

    def __str__(self):
        return (
            "\n".join(str(record) for record in self.data.values())
            if self.data
            else "The address book is empty."
        )
    def _initialize_data(self) -> None:
        self.data = Serializer.load(self.DATA_FILE) or {}
        
    def serialize_data(self) -> None:
        Serializer.save(self.data, self.DATA_FILE)

    def add_record(self, record: Record)->None:
        self.data[record.name.value] = record

    def find(self, name:str)->Record:
        return self.data.get(name)

    def delete(self, name:str)->None:
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Contact not found")

    def save(self) -> Memento:
        return Memento(self.data)

    def restore(self, memento: Memento) -> None:
        self.data = memento.get_state()


    def get_all_contacts_as_list(self) -> list[dict]:
        contacts_list = []
        for record in self.data.values():
            contact_dict = {
                "name": record.name.value,
                "phones": [phone.value for phone in record.phones],
                "birthday": (
                    record.birthday.value if record.birthday else None
                ),
            }
            contacts_list.append(contact_dict)
        return contacts_list

    def get_upcoming_birthdays(self) -> list[dict]:
        return BirthdayHelper().get_upcoming_birthdays(self.get_all_contacts_as_list())
