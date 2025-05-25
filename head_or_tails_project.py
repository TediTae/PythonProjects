import random

random_number = random.random() * 10

random_number = round(random_number)

if random_number <= 5:
    print("Tails")
else:
    print("Head")
