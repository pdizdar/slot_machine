import random #to pick the value of slot machine randomly


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2

}

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

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # .items give you both key n value associated with the key
        for _ in range(symbol_count): # use _instead of i for looop
            all_symbols.append(symbol)

    columns = [] 
    for _ in range(cols): #generate column
        column =[]
        current_symbols = all_symbols[:] #[:] means a copy # 
        for _ in range(rows):
            value = random.choice(current_symbols) #picks random value from the list
            current_symbols.remove(value) 
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end='|')
            else:
                print(column[row], end='')
        
        print()

def deposit():
    while True: #continue asking for valid amount 
        amount = input('What would you like to deposit? $')
        if amount.isdigit(): # to check amount is actually a number
            amount = int(amount) #if its a valid whole number then convert into integer
            if amount > 0: #check if amount is greater than 0
                break # break the while loop
            else: 
                print('Amount must be greater than 0.')
        else:
            print('Please enter a number.')

    return amount

def get_number_of_lines():
    while True: #continue asking for valid amount 
        lines = input('Enter the number of lines to bet on (1-' + str(MAX_LINES) + ')? ') #bet in between 1-maxline
        if lines.isdigit(): # to check amount is actually a number
            lines = int(lines) #if its a valid whole number then convert into integer
            if 1 <= lines <= MAX_LINES: # to check if lines is inbetween these two number
                break # break the while loop
            else: 
                print('Enter a valid number of lines.')
        else:
            print('Please enter a number.')

    return lines

def get_bet():
    while True:
        amount = input('What would you like to bet on each line? $')
        if amount.isdigit(): 
            amount = int(amount) 
            if MIN_BET <= amount <= MAX_BET: # check if the bet is in between min_bet and max_bet
                break 
            else: 
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}.')
        else:
            print('Please enter a number.')

    return amount

def spin(balance):
    
    lines = get_number_of_lines()
    while True: #to check if someone tries to bet more than the balance
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f'You do not have enough to bet that amount, your current balance is: ${balance}')
        else:
            break

    print(f'You are betting ${bet} on {lines} lines. Toal bet is equal to: ${total_bet}')

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'You won ${winnings}.')
    print(f'You won on lines:', *winning_lines) # *runs multiple line
    return winnings - total_bet

    #print(balance , lines)

def main():
    balance = deposit()
    while True:
        print(f'Current balance is ${balance}')
        answer = input("Press enter to play (q to quit).")
        if answer =='q':
            break
        balance += spin(balance)
    #print(balance , lines)
    print(f'You left with ${balance}')

main()