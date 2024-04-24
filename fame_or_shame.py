import os


def signature_grades():
    global total
    while True:
        total = 0
        try:
            for i in range(0, amount):
                grades = float(input(f"Enter grade #{i+1}: "))
                percentage = (float(input(f"- Enter grade #{i+1} percentage: "))/100) * grades
                total += percentage
            break
        except(ValueError, EOFError, KeyboardInterrupt):
            clear_terminal()
            print("----- only NUMBERS are allowed -----")
    return total


def approach():
    global total
    clear_terminal()
    decimal_1 = int(total*10) % 10
    decimal_2 = int(total*100) % 10
    if decimal_1 in decimals_list[0:9] and decimal_2 in up_decimals:
        total = float(f"{int(total)}.{decimal_1+1}")
    elif decimal_1 == 9 and decimal_2 in up_decimals:
        total = float(f"{int(total+1)}.{decimal_1-decimal_1}")
    elif decimal_1 in decimals_list and decimal_2 in down_decimals:
        total = float(f"{int(total)}.{decimal_1}")
    if(total >= 3.0):
        return f"----- your GPA is {total}, now you can rest -----"
    else:
        return f"----- your GPA is {total}, you'll have to repeat -----"
    

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    decimals_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    up_decimals = [5, 6, 7, 8, 9]
    down_decimals = [0, 1, 2, 3, 4]
    while True:
        while True:
            try:
                amount = int(input("Enter amount of grades: "))
                clear_terminal()
                if amount < 0:
                    print("----- only POSITIVE numbers are allowed -----")
                else:
                    break
            except(ValueError, EOFError, KeyboardInterrupt):
                clear_terminal()
                print("------ only INT numbers are allowed -----")
        signature_grades()
        print(approach())
        try:
            another = input("""
Want to continue?
- "1" to yes
- Another key to exit

Enter your choice: """)
            clear_terminal()
            if another == "1":
                continue
            else:
                print("----- see you space, cowboy -----")
                break 
        except(ValueError, EOFError, KeyboardInterrupt):
            clear_terminal()
            print("----- uknown error -----")
            continue