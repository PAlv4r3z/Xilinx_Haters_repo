def calculator(operation, num1, num2):  #Evaluates operation and performs the specified operation with the numbers given
    if operation == 0:
        return add(num1, num2)
    if operation == 1:
        return substract(num1, num2)
    if operation == 2:
        return multiply(num1, num2)
    if operation == 3:
        return divide(num1, num2)

operation = input("Type in 0 for +, 1 for -, 2 for * and 3 for /:" )
num1 = input("Insert your first number: ")
num2 = input(("Insert your first number: ")
print(calculator(operation, num1, num2))
