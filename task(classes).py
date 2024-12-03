from collections import UserDict

class Field:
    def __init__(self, value:str):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value:str):
        self.value = value
  
class Phone(Field):
    def __init__(self, value:str):
        if len(value) == 10:  # checking l
           self.value = value
        else:
            raise ValueError
 
    def __eq__(self, value: object) -> bool:
        return self.value == value
        

class Record:
    def __init__(self, name:str):
        self.name = Name(name)
        self.phones = []

    

    def add_phone(self, phone:str):
        self.phones.append(Phone(phone))
        
    
    def remove_phone(self, phone:str):
        phone = Phone(phone)
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            return f"Phone {phone} is not in record"
        
    def edit_phone(self, old_phone:str, new_phone:str):
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)
        if old_phone in self.phones:
            self.phones.remove(old_phone)
            self.phones.append(new_phone)

    def find_phone(self, phone:str):
        phone = Phone(phone)
        if  phone in self.phones:
            return phone
        return None


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}


    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        if name in self.data.keys():
            return self.data[name]
        return None
    
    def delete(self, name:str):
        record = Record(Name(name))
        self.data.get(record.name.value)

    def __str__(self):
        return  '\n'.join([str(i) for i in self.values()])
    
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")

john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
print(john_record)
book.add_record(john_record)
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
print(jane_record)
book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
print(book)
john = book.find("John")
print(john)
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")
john_record.remove_phone("1234567890")
print(john_record)
john_record.edit_phone("5555555555", "0987654321")
print(john_record)
john_record.edit_phone("0987654321", "04545454")