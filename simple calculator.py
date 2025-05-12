def simple_calculator():
    print("Simple Calculator (+, -, *, / between two numbers)")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return
        else:
            print("Only +, -, *, or / operators are allowed.")
            return

        print("Result:", result)

    except ValueError:
        print("Please enter valid numbers.")

# Run the calculator
simple_calculator()