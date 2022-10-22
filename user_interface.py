import controller as cr
import logger as lg


def ls_directory():
    while True:
        print(
            '\nСontents:\n\
            1 - Show the directory\n\
            2 - Search by phone number\n\
            3 - Add a new entry\n\
            4 - Delete an entry\n\
            5 - Close the directory\n')

        num = check_input(input('Select a menu item: '))

        if num == 1:
            lg.write_log('The user has selected 1 - Show the directory')
            print(cr.retrive())

        elif num == 2:
            lg.write_log('The user has selected 2 - Search by phone number')
            search = input('Enter the phone number: ')
            lg.write_log(f'User entered: {search}')
            print(cr.retrive(number=search))

        elif num == 3:
            lg.write_log('The user has selected 3 - Add a new entry')
            name = input('Enter a name: ')
            lg.write_log(f'User entered: {name}')
            surname = input('Enter a surname: ')
            lg.write_log(f'User entered: {surname}')
            number = input('Enter a telephone number: ')
            lg.write_log(f'User entered: {number}')
            email = input('Enter a email: ')
            lg.write_log(f'User entered: {email}')
            cr.create(name, surname, number, email)

        elif num == 4:
            lg.write_log('The user has selected 4 - Delete an entry')
            print('1 - Find a number by surname')
            print('2 - Find a number by name')
            print('3 - Search by phone number')
            del_data = check_input(input('Select a menu item: '))

            if del_data == 1:
                lg.write_log('The user has selected item 4 - Delete an entry 1 - Find a number by surname')
                search = input('Enter a surname: ')
                lg.write_log(f'User entered: {search}')
                print(cr.retrive(surname=search))
                user_id = input('Enter a id: ')
                lg.write_log(f'User entered: {user_id}')
                cr.delete(id=user_id)

            elif del_data == 2:
                lg.write_log('The user has selected item 4 - Delete an entry 2 - Find a number by name')
                search = input('Enter a name: ')
                lg.write_log(f'User entered: {search}')
                print(cr.retrive(name=search))
                user_id = input('Enter a id: ')
                lg.write_log(f'User entered: {user_id}')
                cr.delete(id=user_id)

            elif del_data == 3:
                lg.write_log('The user has selected 4 - Delete an entry 3 - Search by phone number')
                search = input('Enter a phone number: ')
                lg.write_log(f'User entered: {search}')
                print(cr.retrive(number=search))
                user_id = input('Enter a id: ')
                lg.write_log(f'User entered: {user_id}')
                cr.delete(id=user_id)

            else:
                lg.write_log(f'User entered an invalid menu value {num}')
                print(f'\nThere is no such item {num}.\nSelect a menu item.')

        elif num == 5:
            lg.write_log('Close the directory')
            print('The contents closed')
            break

        else:
            lg.write_log(f'User entered an invalid menu value: {num}')
            print(f'\nТhere is no such item {num}.\nSelect a menu item.')


def check_input(symbol):
    while symbol.isdigit() != True:
        lg.write_log(f'The user entered not a digit: {symbol}')
        print('\nYou entered not a digit.')
        symbol = input('Select a menu item: ')
    return int(symbol)