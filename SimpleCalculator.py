#SimpleCalculator

while True:
    while True:
        # Deciding which operation is the program going to use
        operation = input("Insert the operation (+, -, *, /): ")
        if operation in ["+", "-", "*", "/"]:
            break
        else:
            print("Invalid input. Please try again.")

    # Inputs of numbers
    num1 = float(input("Insert the first number: "))
    num2 = float(input("Insert the second number: "))

    # Printing the result
    if operation == "+":
        result = num1 + num2
        print("The result is:", round(result, 2))
    elif operation == "-":    
        result = num1 - num2
        print("The result is:", round(result, 2))
    elif operation == "*":
        result = num1 * num2
        print("The result is:", round(result, 2))
    elif operation == "/":   
        result = num1 / num2
        print("The result is:", round(result, 2)) 

    # Option for repeating the process or shutting down
    another_calculation = input("Do you want to calculate another pair of numbers? (Y/N): ").capitalize()
    if another_calculation != 'Y':
        break