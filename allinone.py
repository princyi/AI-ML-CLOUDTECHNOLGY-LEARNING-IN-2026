# only using concadation + function + loop .
# creating a slot machine game 
# by using noemal python code
import random

MAX_LINE = 3
MAX_BET = 1000
MIN_BET = 2

ROWS = 3
COLS = 3

symbol_count ={
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8,
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2,
}

# check the winnings 
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# adding the symbols value
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbols, symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbols)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns
# creat colom and row for slot machine
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()



# for deposite code 
def deposite (amount):
    while True:
        amount = input("what would you like to deposite $ ")
        if amount.isdigit():  # uses to check is this input or not by isdigit() method
            amount = int(amount)   # type conversion done here str to int 
            if amount > 0:
                break
            else:
                print("aount is greater than 0.")
        else:
            print("pleas enter a number")

    return amount 

# for deposite amount 
def num_of_lines():
    while True:
        lines = input("Enter a number to bet on (1-" + str(MAX_LINE) + ")? ")
        if lines.isdigit():  # uses to check is this input or not by isdigit() method
            lines = int(lines)   # type conversion done here str to int 
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():  # uses to check is this input or not by isdigit() method
            amount = int(amount)   # type conversion done here str to int 
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def main():
    balance = deposite(0)
    lines = num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount. Your current balance is: ${balance}")
        else:
            break      
    bet = get_bet()
    total_bet = bet * lines
    print(f"you are beting ${bet} on {lines} lines. Total bet is equal to: $ {total_bet} ")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


main()


    








