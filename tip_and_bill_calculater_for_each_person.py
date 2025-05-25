print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
final_bill = bill * tip / 100 + bill
pay_for_each = final_bill / people
each_person_final_bill = round(pay_for_each, 2)
print(f"Each person should pay : ${each_person_final_bill}")
