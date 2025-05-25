import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# chosen_letters = ""
#
# for letter in letters:
#     if nr_letters > 0:
#        chosen_letters += random.choice(letters)
#        nr_letters -= 1
#
# chosen_numbers = ""
#
# for number in numbers:
#     if nr_numbers > 0:
#         chosen_numbers += random.choice(numbers)
#         nr_numbers -= 1
#
# chosen_symbols = ""
#
# for symbol in symbols:
#     if nr_symbols > 0:
#         chosen_symbols += random.choice(symbols)
#         nr_symbols -=1
#
# final_password = chosen_letters + chosen_symbols + chosen_numbers
#
# password_list = list(final_password)
# random.shuffle(password_list)
# password_final = ''.join(password_list)
# print(password_final)

####################################################################
#BETTER VERSION
####################################################################

password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append((random.choice(symbols)))

for char in range(0, nr_numbers):
    password_list.append((random.choice(numbers)))

random.shuffle(password_list)
password = ''.join(password_list)
print(password)

