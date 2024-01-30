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
amount_deposited = deposit()
print("Deposited amount:", amount_deposited)
