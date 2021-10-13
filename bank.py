def bank_assign():

    print("Welcome to MollyKate's Bank ATM")
    balance = 0


    choice = ''

    def user_balance():
        global balance 
        print(f'Available funds: $ {balance:,.2f}')
    def user_deposit():
        global balance 
        deposit_amount = (int(input("Enter deposit amount: ")))
        balance = deposit_amount + balance
        print(f'Your new balance is: $ {balance:,.2f}')
    def user_withdraw():
        global balance 
        withdrawl_amount = (int(input("Enter withdrawl amount: ")))
        if balance <= withdrawl_amount:
            print(f'Adequate funding not available. Your current balance is $ {balance:,.2f}.')
        else:
            balance = balance - withdrawl_amount
            print(f'Your new balance is: $ {balance:,.2f}')


    while choice.upper() != 'Q':
        choice = input(""""Please select from the following menu options: "
        (B)alance
        (D)eposit
        (W)ithdraw
        (Q)uit
        """)
        
        if choice.upper() == 'B':
            user_balance()

        if choice.upper() == 'D':
            user_deposit()

        if choice.upper() == 'W':
            user_withdraw()

        if choice.upper() == 'Q':
            print("Have a nice day! \nGoodbye")
            
    return

