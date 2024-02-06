from collections import UserDict


class Field:
    def __init__(self, value=None):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):

        self.phones.append(Phone(phone))

    def remove_phone(self, address_book):
        name = self.name.value
        if name in address_book.data:
            del address_book.data[name]
        else:
            raise KeyError

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone


class AddressBook(UserDict):
    def add_record(self, record):
        key = record.name.value
        self.data[key] = record

    def find_record(self, name):
        record = self.data.get(name)
        if record:
            return record
        else:
            return None


def main():
    address_book = AddressBook()

    while True:
        try:
            command = input("Enter command: ")

            if command == "hello":
                print("How can I help you?")

            elif command.startswith("add"):

                _, first_name, last_name, phone_number = command.split(" ", 3)

                name = f'{first_name} {last_name}'
                record = Record(name)
                record.add_phone(phone_number)
                address_book.add_record(record)
                print("Contact added successfully.")

            elif command.startswith("change"):
                _, first_name, last_name, new_phone_number = command.split(
                    " ", 3)
                name = f'{first_name} {last_name}'
                record = address_book.find_record(name)
                if record:
                    record.edit_phone(record.phones[0].value, new_phone_number)
                    print("Phone number updated successfully.")
                else:
                    print("Contact not found.")

            elif command.startswith("find"):
                _, first_name, last_name = command.split(" ", 2)
                name = f'{first_name} {last_name}'
                found_records = address_book.find_record(name)
                if found_records:
                    for phone in found_records.phones:
                        print(f'{
                              found_records.name.value} Phone: {phone.value}')

                else:
                    print("Contact not found.")

            elif command.startswith("delete"):
                _, first_name, last_name = command.split(" ", 2)
                name = f'{first_name} {last_name}'
                record = address_book.find_record(name)
                if record:
                    record.remove_phone(address_book)
                    print('Contact delete successfully')

                else:
                    print("Contact not found.")
            elif command in ["good bye", "close", "exit", "."]:
                print("Good bye!")
                break
            else:
                print("Invalid command. Please try again.")
        except Exception as e:
            print(f'Error: {e}')


if __name__ == "__main__":
    main()
