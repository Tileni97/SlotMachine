import random

# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
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

def check_winnings(columns, lines, bet, value):
    winnings = 0
    winnings_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        
        for col_index, column in enumerate(columns):
            symbol_to_check = column[line]
            
            if symbol != symbol_to_check:
                symbol = None
                break
        else:
            winnings += value[symbol] * bet 
            winnings_lines.append(line + 1)

    return winnings, winnings_lines

            

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)  # Use current_symbols instead of all_symbols
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)  # Append the column to columns list

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
               print(column[row], end=" | ")
            else:
               print(column[row], end=" ")

        print()      

           


def deposit():
    while True:
        amount_str = input("Enter amount to deposit: ")
        
        if amount_str.isdigit():
            amount = int(amount_str)
            
            if amount > 0:
                break
            else:
                print("Please enter an amount greater than 0")
        else:
            print("Please enter a valid positive integer")

    return amount

# Test the deposit function
#amount_deposited = deposit()
#print("Deposited amount:", amount_deposited)

def get_bet():
    while True:
        bet_str = input(" What would you like to bet on each line? N$")
        
        if bet_str.isdigit():
            bet = int(bet_str)
            
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please enter an amount between N${MIN_BET} and N${MAX_BET}")
        else:
            print("Please enter a valid positive integer")

    return bet

def get_number_of_lines():
    while True:
        lines = input("Enter the amount of lines to bet on (1-" + str(MAX_LINES) + ")?  ")
        
        if lines.isdigit():
            lines = int(lines)
            
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines")
        else:
            print("Please enter a number of lines")

    return lines

def spin(balance):
     lines = get_number_of_lines()
     while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: N${balance}")
        else:
            break

     print(f"You are betting ${bet} on {lines} lines. Total bet is equal to : N${total_bet} ")

     slots = get_slot_machine_spin(ROWS, COLS, symbol_count)

     print_slot_machine(slots)
     winnings, winnings_lines= check_winnings(slots, lines, bet, symbol_value)  
     print(f"You won N${winnings}.")
     print(f"You won on lines: {', '.join(map(str, winnings_lines))}")
     return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Your current balance is: N${balance}")
        answer = input("Would you like to still play? (Y/N) ")
        if answer == "Y":
            balance += spin(balance)
        elif answer == "N":
            print(f"Your final balance is: N${balance}")
            break
        else:
            print("Please enter a valid input")


main()
