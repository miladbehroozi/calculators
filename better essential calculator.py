def calculate(expression):
    import re

    # Split numbers and operators
    tokens = re.findall(r'\d+\.?\d*|[+\-*/]', expression)

    # Step 1: Process * and /
    i = 0
    while i < len(tokens):
        if tokens[i] == '*':
            result = float(tokens[i - 1]) * float(tokens[i + 1])
            tokens[i - 1:i + 2] = [str(result)]
            i = 0  # reset to start
        elif tokens[i] == '/':
            if float(tokens[i + 1]) == 0:
                return "Error: Division by zero"
            result = float(tokens[i - 1]) / float(tokens[i + 1])
            tokens[i - 1:i + 2] = [str(result)]
            i = 0
        else:
            i += 1

    # Step 2: Process + and -
    result = float(tokens[0])
    i = 1
    while i < len(tokens):
        op = tokens[i]
        num = float(tokens[i + 1])
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        i += 2

    return result

def essential_calculator_v_2():
    print("essential Calculator (supports +, -, *, / with proper order)")

    expression = input("Enter your expression: ").replace(" ", "")
    result = calculate(expression)
    print("Result:", result)

# Run the calculator
essential_calculator_v_2()