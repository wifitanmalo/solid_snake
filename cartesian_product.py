import os


def set_items():
    global number, word
    number = []
    word = []
    while True:
        try:
            amount = int(input("Enter the number of items: "))
            if amount < 0:
                clear_terminal()
                print("----- only positive amount -----")
            else:
                break
        except(ValueError, EOFError, KeyboardInterrupt):
            clear_terminal()
            print("----- unknown error -----")
    for i in range(1, amount+1):
        item = input(f"- Enter the item #{i}: ")
        if (item not in number) and (item.isdigit()):
            number.append(item)
        elif (item not in word) and (item.isalpha()):
            word.append(item.lower())
    return number, word

    
def order_numbers():
    for i in range(0, len(number)):
        position = i
        current = number[i]
        while((position > 0) and (number[position-1] > current)):
            number[position] = number[position-1]
            position -= 1
        number[position] = current
    return number


def order_words():
    abc = "abcdefghijklmnñopqrstuvwxyz"
    for i in range(0, len(word)):
        position = i
        current = word[i]
        while((position > 0) and (word[position-1] > current)):
            word[position] = word[position-1]
            position -= 1
        word[position] = current
    return word


def cartesian_product():
    global cartesian
    cartesian = []
    for set_one in range(0, len(first_set)):
        for set_two in range(0, len(second_set)):
            if (first_set[set_one] == second_set[set_two]):
                product = [first_set[set_one]]
                cartesian.append(product)
            else:
                product = [first_set[set_one], second_set[set_two]]
                cartesian.append(product)
    return cartesian


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    first_set = []
    second_set = []
    for set_number in range(0, 2):
        clear_terminal()
        if (set_number == 0):
            print("----- First set -----")
        else:
            print("----- Second set -----")
        set_items()
        order_numbers()
        order_words()
        if set_number == 0:
            first_set = number + word
        elif set_number == 1:
            second_set = number + word
    clear_terminal()
    print(
f"""
FIRST SET: {first_set}
SECOND SET: {second_set}
CARTESIAN PRODUCT: {cartesian_product()}
""")