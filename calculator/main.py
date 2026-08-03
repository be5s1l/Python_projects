from art import logo

def sum(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

operations = {
    "+" : sum,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    continue_calc = True
    num1 = float(input("Enter first number: "))

    while continue_calc:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Enter second number: "))
        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = result
        else:
            continue_calc = False
            print("\n" * 30)
            calculator()

calculator()