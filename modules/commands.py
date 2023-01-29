import os
import sqlite3
from prettytable import PrettyTable
from colorama import Fore, Style
from .help import help_command


command_list = ["create", "delete", "update", "find", "preview", "exit", "help", "clear"]

command_requirements = {
    "create": 5,
    "delete": 2,
    "update": 3,
    "find": 3,
    "help": 1
}

tab = PrettyTable(['ID', 'Name', 'Address', 'Phone', 'Email'])


def create(name, address, phone, email):
    if not (check_existence("Name", name)):
        cursor.execute(f"INSERT INTO contact_info (Name, Address, Phone, Email) VALUES ('{name}', '{address}', '{phone}', '{email}')")
        conn.commit()
    else:
        print(f"contact with name {name} already exist")


def check_existence(data_type, data_value, all=False):
    if not all:
        cursor.execute(f"SELECT * FROM contact_info WHERE {data_type.capitalize()} = '{data_value}'")
        return not len(cursor.fetchall()) == 0
    else:
        cursor.execute(f"SELECT * FROM contact_info")
        return not len(cursor.fetchall()) == 0


def update(name, data_type):
    try:
        if not (check_existence("Name", name)):
            print('Contact does not exist')
        else:
            new_data = input("Enter the new data you want to change to: ")

            for old_data in cursor.execute(f"SELECT {data_type} FROM contact_info WHERE Name = '{name}'"):
                print('changes:')
                print(Fore.RED + old_data[0], end='')
                print(Style.RESET_ALL, end='')
                print('   --->   ', end='')
                print(Fore.LIGHTGREEN_EX + new_data, end='')
                print(Style.RESET_ALL)
            cursor.execute(f"UPDATE contact_info SET {data_type.capitalize()} = '{new_data}' WHERE Name = '{name}'")
            conn.commit()
    except sqlite3.OperationalError:
        print(f'There are no columns named {data_type}')
        print('You must select from Name, Address, Phone & Email')


def delete(id):
    cursor.execute(f"DELETE FROM contact_info WHERE ID = '{id}'")
    conn.commit()


def search(data_type, data_val):
    for row in cursor.execute(f"SELECT * FROM contact_info WHERE {data_type.capitalize()} LIKE '%{data_val}%'"):
        tab.add_row(list(row))
    print(tab)
    tab.clear_rows()


def execute(command):

    if len(command) > 0 and command[0] in command_list:
        if len(command) < command_requirements[command[0]]:
            print("More information required to execute the given command")
            print(f"Type help or help {command[0]} for more information")
        else:
            match command[0]:
                case "create":
                    create(command[1], command[2], command[3], command[4])
                case "delete":
                    delete(command[1])
                case "update":
                    update(command[1], command[2])
                case "find":
                    search(command[1], command[2])
                case "help":
                    try:
                        help_command(command[1])
                    except IndexError:
                        help_command()
    else:
        print("Invalid command")


if __name__ != "__main__":
    os.makedirs('Contacts', exist_ok=True)

    conn = sqlite3.connect('Contacts/contacts.db')

    cursor = conn.cursor()

