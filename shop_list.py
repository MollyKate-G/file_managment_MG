def shopping_list():

    print("Shopping List!\n")

    choice = " " 
    while choice.upper() != 'Q':
        choice = input("""--------------------------\n\nChoose an option: 
        (P)rint shopping list
        (A)dd item to shopping list
        (C)lear shopping list
        (Q)uit
        """)

        if choice.upper() == 'P':
            with open("shopping_list.txt", "r") as my_file:
                print(my_file.read())    

        if choice.upper() == 'A':   
            shop_item = input("Enter shopping list item: ")
            with open("shopping_list.txt", "a") as my_file:
                my_file.write(f'\n{shop_item}\n')
                print(f"\n{shop_item}, have been added to your shopping list\n")

        if choice.upper() == 'C':
            erase_shopping = " "
            erase_shopping = input("Are you sure you want to delete your shopping list? Y/N \n")
            if erase_shopping.upper() == 'Y':
                print("Your shopping list has been cleared")
                with open("shopping_list.txt", "w") as my_file:
                    my_file.write(" ")    
            else:
                print("Your shopping list is still saved")

        if choice.upper() == 'Q':
            print("Exiting the program. Your shopping list has been saved in 'shopping_list.txt'. Goodbye!")
            
        return

