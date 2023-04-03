from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return str(self)
    
class Name(Field):
    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return "Name: " + super().__str__()
    
class Phone(Field):
    def __init__(self, value=None):
        super().__init__(value)

    def __str__(self):
        return "Phone: " + super().__str__()
    
class Record:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone if phone is not None else []
        
    def add_phone(self, phone:Phone):
        self.phone.append(phone)
        
    def del_phone(self, phone):
        self.phone.remove(phone)
        
    def edit_phone(self, old_phone, new_phone):
        index = self.phone.index(old_phone)
        self.phone[index] = new_phone
        
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record