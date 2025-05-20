print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Young tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")

    photo_want = str(input("You want a photo for $3, If you want type y for YES or type n for NO."))

    if photo_want == "y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
