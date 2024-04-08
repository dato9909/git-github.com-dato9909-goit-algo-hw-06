from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
        def __init__(self, value):
            if len(value) == 10 and value.isdigit():                   
                super().__init__(value)
            else:
                  raise ValueError('Неправильный телефон')

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        self.phones = [p for p in self.phones if str(p) != phone_number]

    def find_phone(self, phone_number):
       for phone in self.phones:
           if str(phone) == phone_number:
               return phone
       return None
    
    def change_phone(self, old_number, new_number):
       for i, phone in enumerate(self.phones):
           if str(phone) == old_number:
               self.phones[i] = Phone(new_number)
               return True
       return False
    


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find_record(self, name):
        return self.data.get(name)
    
    def delete_record(self, name):
        if name in self.data:
            del self.data[name]

         
    
    def change_number(self, record, old_number, new_number):
        if record.name.value in self.data:
            if record.change_phone(old_number, new_number):
                print("Номер успешно изменен.")
            else:
                print("Телефон не найден.")
        else:
            print("Запись не найдена.")


def main():
    # Создаем новую адресную книгу
    book = AddressBook()

    # Создаем записи для контактов
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")

    # Добавляем записи в адресную книгу
    book.add_record(john_record)
    book.add_record(jane_record)

    # Выводим все записи в книге
    for name, record in book.data.items():
        print(record)

    # Изменяем номер телефона у записи John
    book.change_number(john_record, "1234567890", "1112223333")

    # Поиск записи John
    found_record = book.find_record("John")
    if found_record:
        print("Найдена запись John:", found_record)
    else:
        print("Запись John не найдена.")

    # Удаляем запись Jane
    book.delete_record("Jane")

if __name__ == "__main__":
    main()


        






"""
# Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

"""