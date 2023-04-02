from classes import AddressBook, Record, Name, Phone


contacts = AddressBook()


def input_error(func):
    
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params. Print help"
        except KeyError:
            return 'Contact  not found, try again or use help'
        except AttributeError:
            return 'Contact  not found, try again or use help'
    return inner


@input_error
def add(*args):
    list_of_param = args[0].split()
    name = list_of_param[0]
    phone_number = [Phone(phone) for phone in list_of_param[1:]]
    record = Record(name, phone_number)
    contacts.add_record(record)
    if not phone_number:
        raise IndexError()
    
    return f'{name}, phone number {phone_number[0]}'


def show_all(*args):
    if not contacts.data:
        return 'Not contacts'
    return '\n'.join(f'{k}: {", ".join(str(phone) for phone in v.phone)}' for k, v in contacts.data.items())


@input_error
def phone(*args):
    list_of_param = args[0].split()
    name = Name(list_of_param[0])
    record = contacts.get(name.value)
    phone_number = record.phone[0]
    return f'{phone_number}'


@input_error
def change(*args):
    list_of_param = args[0].split()
    name = Name(list_of_param[0])
    phone_number = [Phone(phone) for phone in list_of_param[1:]]
    if contacts.get(name.value):
        contacts.data[name.value].phone = phone_number
        return f'Contact {name.value} update {str(phone_number[0])}'


def exit(*args):
    return "Good bye!"


def no_command(*args):
    return 'Unknown command, try again or help'


def help(*args):
    return "If there are problems, read the file, readme!"


def hello(*args):
    return "How can I help you?"


COMMANDS = {help: 'help',
            hello: 'hello',
            add: 'add',
            show_all: 'show all',
            phone: 'phone',
            change: 'change',
            exit: 'exit'}


def command_handler(text):
    for command, kword in COMMANDS.items():
        if text.startswith(kword):
            return command, text.replace(kword, '').strip()
    return no_command, None


def main():
    print('Hello user!')
    while True:
        
        user_input = input('>>>')
        command, data = command_handler(user_input)

        print(command(data))
        
        if user_input == 'exit':
            break 
            

if __name__ == '__main__':
    main()