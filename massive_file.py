import binary_calc 
import bank
import magic_8_ball
import shop_list
import calendar

choice =''
while choice.upper() != 'Q':
    choice = input(""""What program would you like to run? "

    (1)Binary Calculator
    (2)ATM Bank Assignment
    (3)Magic 8 Ball
    (4)Shopping List
    (5)Calendar Project
    (6)Quit
    """)
    
    if choice.upper() == '1':
        binary_calc.menu() 
    if choice.upper() == '2':
        bank.bank_assign()
    if choice.upper() == '3':
        magic_8_ball.magic()
    if choice.upper() == '4':
        shop_list.shopping_list()
    if choice.upper() == '5': 
        calendar.calendar()
    if choice.upper() == '6':
        print("\nGoodbye")
