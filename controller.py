import csv
import os.path

db_file_name = ''
db = []
id_number = 0


def init_data_base(file_name='db.csv'):
    global id_number
    global db
    global db_file_name
    db_file_name = file_name
    db.clear()
    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if(row[0] != 'ID'):
                    db.append(row)
                    if(int(row[0]) > id_number):
                        id_number = int(row[0])
    else:
        open(db_file_name, 'w', newline='').close()


def create(name='', surname='', number='', email=''):
    global id_number
    global db
    global db_file_name
    if(name == ''):
        print("You have not entered 'name'")
        return
    if(surname == ''):
        print("You have not entered 'surname'")
        return
    if(number == ''):
        print("You have not entered 'telephone number'")
        return
    if(email == ''):
        print("You have not entered 'email'")
        return

    for row in db:
        if(row[1] == name.title() and row[2] == surname.title() and row[3] == number and row[4] == email.lower()):
            print("The contacts already exist")
            return

    id_number += 1
    new_row = [str(id_number), name.title(), surname.title(), number, email.lower()]
    db.append(new_row)
    with open(db_file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)


def retrive(id='', name='', surname='', number='', email=''):
    global id_number
    global db
    global db_file_name
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if(name != '' and row[1] != name.title()):
            continue
        if(surname != '' and row[2] != surname.title()):
            continue
        if(number != '' and row[3] != number):
            continue
        if(email != '' and row[3] != email.lower()):
            continue
        result.append(row)
    if len(result) == 0:
        return f'There is not contact'
    else:
        return result

def delete(id=''):
    global id_number
    global db
    global db_file_name
    if(id == ''):
        print('specify id for delete')
        return

    for row in db:
        if (row[0] == id):
            db.remove(row)
            break

    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)

