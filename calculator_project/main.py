import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4, 8))


def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()

###########################################################################################
######################### OLD VERSION #####################################################
###########################################################################################

# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return  n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# calculation_dict={
#     "+" : add,
#     "-" : subtract,
#     "*" : multiply,
#     "/" : divide,
# }

# num1 = float(input("Please enter the first number."))
# operator = input("Please enter a mathematical operator. As like '+', '-', '*', '/'.")
# num2 = float(input("Please enter the second number."))
# result = calculation_dict[operator](num1, num2)
# print(f"Your result is: {result}")
# continue_calculation = input("Do you want to continue working with the previous result? Type 'y' for yes, type 'n' for no.")
# keep_calculating = True
# while keep_calculating:
#     if continue_calculation == "y":
#         num1 = result
#         operator = input("Please enter a mathematical operator. As like '+', '-', '*', '/'.")
#         num2 = float(input("Please enter the second number."))
#         new_result = calculation_dict[operator](num1, num2)
#         result = new_result
#         print(f"Your result is: {result}")
#         continue_calculation = input("Do you want to continue working with the previous result? Type 'y' for yes, type 'n' for no.")
#     elif continue_calculation == "n":
#         print(f"Your final result is: {result}")
#         keep_calculating = False
#     else:
#         print("Your input is invalid.")


