import random

file = open('contacts.csv', 'w')
add_data = "ID,Name,Surname,PhoneNumber,email\n"
file.writelines(add_data)

names = ['Noah', 'Amelia', 'Oliver', 'Olivia', 'George']
surnames = ['Smith', 'Jones', 'Williams', 'Taylor']
mails = ['@gmail.com', '@hotmail.com', '@yahoo.com']


def list_numbers():
    ls_phone = random.randint(989000000000, 989999999999)
    return str(ls_phone)

def new_raw():
    raw = ""
    raw += random.choice(names) + ',' + random.choice(surnames) + ',' + \
           list_numbers() + ',' + random.choice(surnames) + random.choice(mails)
    return raw

def get_contacts():
    for i in range(30):
        a = f'{str(i + 1)},{new_raw()}\n'
        file.write(a)
    file.close()

get_contacts()