def bin_sub(bin_str_1, bin_str_2):
  
  max_length = max(len(bin_str_1), len(bin_str_2))
  bin_str_1 = bin_str_1.zfill(max_length)[::-1]
  bin_str_2 = bin_str_2.zfill(max_length)[::-1]
  output = ''
  borrow = 0

  for i in range(max_length):
    num1 = bin_str_1[i]
    num2 = bin_str_2[i]
    
    if borrow == 1:
      if num1 == '1':
        num1 = '0'
        borrow = 0
      else:
        num1 = '1'
    if num1 == num2:
      output += '0'
    elif num1 == '1':
       output += '1'
    else:
      output += '1'
      borrow = 1

  if borrow == 1:
    return "Error: Negative Result"

  return output[::-1]
  
def bin_add(bin_str_1, bin_str_2):
  max_width = max(len(bin_str_1), len(bin_str_2))
  bin_str_1 = bin_str_1.zfill(max_width)
  bin_str_2 = bin_str_2.zfill(max_width)

  output = ''
  carry = 0
  for i in reversed(range(len(bin_str_1))):
    if carry == 0:
        if bin_str_1[i] == '0' and  bin_str_2[i] == '0':
          output = output + '0'
          carry = 0
        elif bin_str_1[i] == '1' and  bin_str_2[i] == '1':
          output += '0'
          carry = 1
        else:
          output += '1'
          carry = 0
    else:
        if bin_str_1[i] == '0' and  bin_str_2[i] == '0':
          output = output + '1'
          carry = 0
        elif bin_str_1[i] == '1' and  bin_str_2[i] == '1':
          output += '1'
          carry = 1
        else:
          output += '0'
          carry = 1
  if carry == 1:
    output += '1'
  return output[::-1]

# bin_str = input('Enter a binary number: ')

def bin_inverse():
  bin_str = input('Enter a binary number to inverse: ')
  bin_str_1 = ''
  bin_str_2 = '1'
  new_bin = ''

  if bin_str[0] == '1':
    new_bin = bin_sub(bin_str, bin_str_2)
    for char in new_bin:
      if char == '0': 
        bin_str_1 += '1'
      else: 
        bin_str_1 += '0'
    return(bin_str_1)
    
  else:
    for char in bin_str:
        if char == '0': 
          bin_str_1 += '1'
        else: 
          bin_str_1 += '0'
    bin_str_1 = bin_add(bin_str_1, bin_str_2)
    return (bin_str_1)

  print(bin_inverse(bin_str))

def bin_to_dec(bin_str):
  answer = int(bin_str, 2)
  return answer

def dec_to_bin(dec_num):
  global user_input
  if user_input > 255:
    print('Number out of range')
  if user_input >= 128:
    user_input = user_input - 128
    num_8 = 1
  else:
    num_8 = 0
  if user_input >= 64:
    user_input= user_input - 64
    num_7 = 1
  else:
    num_7 = 0

  if user_input >= 32:
    user_input = user_input - 32
    num_6 = 1
  else:
    num_6 = 0

  if user_input >= 16:
    user_input = user_input - 16
    num_5 = 1
  else:
    num_5 = 0

  if user_input >= 8:
    user_input = user_input - 8
    num_4 = 1
  else:
    num_4 = 0

  if user_input >= 4:
    user_input = user_input - 4
    num_3 = 1
  else:
    num_3 = 0

  if user_input >= 2:
    user_input = user_input - 2
    num_2= 1
  else:
    num_2 = 0

  if user_input > 0:
    user_input = user_input - 1
    num_1 = 1
  else:
    num_1 = 0
  
  print(f'{num_8}{num_7}{num_6}{num_5}{num_4}{num_3}{num_2}{num_1}')

def bin_div(bins_str_1, bin_str_2):
  output = ''
  numer_str = ''
  format_str1 = bin_str_1.zfill(8)
  format_str2 = bin_str_2.zfill(8)
  num_1_list = list(format_str1)

  if int(bin_str_2) == 0:
    print('Undefined')
  for i in range(len(num_1_list)):
    numer_str += num_1_list[i]
    if int(numer_str) < int(format_str2):
      output += '0'
    else:
      output += '1'
      numer_str = str(int(numer_str) - int(format_str2))
  return output

def bin_mul(bin_str_1, bin_str_2):
  to_sum = []

  for index, digit in enumerate(reversed(bin_str_2)):
    row = ''
    for i in bin_str_1:
      if int(digit) and int(i):
        row += '1'
      else:
        row += '0'
    row += '0' * index
    to_sum.append(row)

  output = to_sum[0]
  for i in range(1, len(to_sum)):
    output = bin_add(output, to_sum[i])
  return output 

def menu():
  choice = ''
  while choice.upper() != 'Q':
    choice = input(""""Please select from the following menu options: "

    (B)inary to Decimal Conversion
    (D)ecimal to Binary Conversion
    (A)dd two Binary Numbers
    (S)ubtract two Binary Numbers
    (M)ultiply two Binary Numbers
    D(i)vide two Binary Numbers
    I(n)verse Binary
    (Q)uit
    """)

    if choice.upper() == 'B':
      bin_str = input("Enter a binary number: \n")
      print(f'Your binary number ({bin_str}) converted to a decimal number is {bin_to_dec(bin_str)}\n')
    
    if choice.upper() == 'D':
      user_input = int(input("Choose a number between 0-255 to convert to binary numbers: "))
      dec_to_bin(user_input)

    if choice.upper() == 'A':
      bin_str_1 = input("Enter a binary number: ")
      bin_str_2 = input("Enter a secondary binary number: ")
      print(f'You\'re added binary numbers = {bin_add(bin_str_1, bin_str_2)}\n')

    if choice.upper() == 'S':
      bin_str_1 = input("Enter a binary number: ")
      bin_str_2 = input("Enter a secondary binary number: ")
      print(f'You\'re subtracted binary numbers = {bin_sub(bin_str_1, bin_str_2)}\n')

    if choice.upper() == 'M':
      bin_str_1 = input("Enter a binary number: ")
      bin_str_2 = input("Enter a secondary binary number: ")
      print(f'\nYou\'re multiplied binary numbers equals {bin_mul(bin_str_1, bin_str_2)}.\n')

    if choice.upper() == 'I':
      bin_str_1 = input("Enter a binary number: ")
      bin_str_2 = input("Enter a secondary binary number: ")
      print(f'You\'re divided binary numbers = {bin_div(bin_str_1, bin_str_2)}')

    if choice.upper() == 'N':
      print(bin_inverse())

    if choice.upper() == 'Q':
      print("\nGoodbye")
      return
