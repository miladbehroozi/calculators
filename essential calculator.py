def essential_calculator_v_1():
    print("essential Calculator (+, -, *, / with multiple operations)")

    try:
        expression = input("Enter your expression: ")
        result = eval(expression)

        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print("Invalid input:", e)


# Run the calculator
essential_calculator_v_1()