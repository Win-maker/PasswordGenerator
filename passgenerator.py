from random import choice, shuffle

print('Welcome From Password Generator')

letter = int(input('How Many Letters Would You Like In Your Password'))
symbol = int(input('How Many Symbols Would You Like In Your Password'))
number = int(input('How Many Numbers Would You Like In Your Password'))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '%', '^', '&', '*']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

letter_list = []
symbol_list = []
number_list = []

for i in range (0, letter):
    getletter = choice(letters)
    letter_list.append(getletter)

for j in range(0, symbol):
    getsymbol = choice(symbols)
    symbol_list.append(getsymbol)
    

for n in range(0, number):
    getnumber = choice(numbers)
    number_list.append(getnumber)

password = letter_list + symbol_list + number_list

shuffle(password)

finalpass = "".join(password)

print(f'Your password is: {finalpass}')
    
    
    

