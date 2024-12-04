from collections import UserDict

class Field:
    def __init__(self, value:str):
        self.value = value

    def __str__(self):
        return str(self.value)
    
#class ValueError(Exception):
#    pass    

class Name(Field):
    def __init__(self, value:str):
        self.value = value
  
class Phone(Field):
    def __init__(self, value:str):
        if len(value) == 10 and value.isdigit(): # checking
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
        else:
            raise ValueError   

    def find_phone(self, phone:str):
        for  item in self.phones:
            if item == phone:
                return item
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
        self.data.pop(name, None)

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
     
#print(book)
john = book.find("John")
print(john)
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")
#john_record.remove_phone("1234567890")
#print(john_record)
john_record.edit_phone("5555555555", "0987654321")
print(john_record)
#john_record.edit_phone("0987654321", "0454588787")
#john.add_phone('1234567890')
book.delete("Jane")
print(book)