hex_str = 0

def hex_to_dec(hex_str):

    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10 , 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    user_input = input("Enter a hexadecimal value you would like to convert to a decimal: ")
    length = len(user_input) -1

    for digit in user_input:
        hex_str += hex_dict[digit] * 16 ** length
        length -= 1
    return hex_str

print(hex_to_dec(hex_str))

dec_num = int(input("Enter a decimal number to convert to hexadecimal: "))

def dec_to_hex(dec_num):

    values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
    hex = ''

    while(dec_num > 0):
        remainder = dec_num % 16
        hex = values[remainder]+ hex
        dec_num = dec_num//16
        
    return ("Hexadecimal:", hex)
print(dec_to_hex(dec_num))