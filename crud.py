import os
import shutil


def choice_selection():
    global choice
    while True:
        choice = input("Select your choice: ").capitalize()
        if choice in choices_list:
            break
        else:
            clear_terminal()
            print("----- only can enter C, R, U, D or E -----")
    clear_terminal()
    return choice


def create():
    global users_list, number
    while True:
        name = input("Enter the name to create: ").capitalize()
        clear_terminal()
        if name.isalpha():
            break
        else:
            print("----- name only can contain WORDS -----")
    if name in users_list:
        print(f"----- '{name}' was created again -----")
    else:
        print(f"----- '{name}' was created -----")
    number += 1
    users_list |= {number:name}


def read():
    search = input("Enter the name to search: ").capitalize()
    clear_terminal()
    if search in users_list.values():
        for name_number in range(1, number+1):
            if users_list[name_number] == search:
                return(f"- Hi, {search}! \nNAMES LIST: {users_list}")
    else:
        return(f"----- user '{search}' not founded -----")
        


def update():
    update = input("Enter the name to update: ").capitalize()
    if update in users_list.values():
        while True:
            new = input("- Enter the new name: ").capitalize()
            if new.isalpha():
                break
            else:
                clear_terminal()
                print("  ----- name only can contain WORDS -----")
        for name_number in range(1, number+1):
            if users_list[name_number] == update:
                users_list[name_number] = new
                break
        clear_terminal()
        return(f"----- '{update}' was updated to '{new}' -----")
    else:
        clear_terminal()
        return(f"----- user '{update}' not founded -----")


def delete():
    global number
    delete = input("Enter the name to delete: ").capitalize()
    clear_terminal()
    if delete in users_list.values():
        for name_number in range(1, number+1):
            if users_list[name_number] == delete:
                number -= 1
                users_list.pop(name_number)
        return(f"----- '{delete}' was deleted -----")
    else:
        return(f"----- user '{delete}' not founded -----")


def exit():
    farewell = "see you space, cowboy..."
    terminal_width, _ = shutil.get_terminal_size()
    x = terminal_width - len(farewell)
    print(" " * x, end="")
    return farewell


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    

if __name__ == '__main__':
    number = 0
    users_list = {}
    choices_list = ["C", "R", "U", "D", "E"]
    while True:
        try:
            print("""
***** Welcome to the CRUD *****
"C" to create a user
"R" to read a user
"U" to update a user
"D" to delete a user
"E" to exit""")
            choice_selection()
            if choice == "C":
                create()
            elif choice == "R" and len(users_list) > 0:
                print(read())
            elif choice == "U" and len(users_list) > 0:
                print(update())
            elif choice == "D" and len(users_list) > 0:
                print(delete())
            elif choice == "E":
                print(exit())
                break
            else:
                print("----- register a user first -----")
        except(EOFError, KeyboardInterrupt):
            clear_terminal()
            print("\n----- unknown error -----")