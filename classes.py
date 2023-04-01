class UserDict:
    pass

class Field:
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return self.value
    
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
        
    def del_phone(self, phone):
        self.phones.remove(phone)
        
    def edit_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone
        
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record