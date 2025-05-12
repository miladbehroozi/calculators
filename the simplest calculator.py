def simplest_calculator():
    print("Simplest Calculator (Only + or - between two numbers)")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+ or -): ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        else:
            print("Only + or - operators are allowed.")
            return

        print("Result:", result)

    except ValueError:
        print("Please enter valid numbers.")

# Run the calculator
simplest_calculator()