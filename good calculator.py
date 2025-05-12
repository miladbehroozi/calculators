import re

def calculate(expression):
    tokens = re.findall(r'\d+\.?\d*|[+\-*/]', expression)

    # Step 1: Handle * and /
    i = 0
    while i < len(tokens):
        if tokens[i] == '*':
            result = float(tokens[i - 1]) * float(tokens[i + 1])
            tokens[i - 1:i + 2] = [str(result)]
            i = 0
        elif tokens[i] == '/':
            if float(tokens[i + 1]) == 0:
                return "Error: Division by zero"
            result = float(tokens[i - 1]) / float(tokens[i + 1])
            tokens[i - 1:i + 2] = [str(result)]
            i = 0
        else:
            i += 1

    # Step 2: Handle + and -
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

def evaluate_expression(expression):
    # Remove spaces
    expression = expression.replace(" ", "")

    # Resolve parentheses recursively
    while '(' in expression:
        # Find the innermost ( ... )
        inner = re.search(r'\(([^()]+)\)', expression)
        if not inner:
            return "Error: Mismatched parentheses"
        sub_expr = inner.group(1)
        sub_result = calculate(sub_expr)
        expression = expression[:inner.start()] + str(sub_result) + expression[inner.end():]

    # Final evaluation
    return calculate(expression)

def good_calculator():
    print("Simple Calculator with parentheses support")

    expr = input("Enter your expression: ")
    result = evaluate_expression(expr)
    print("Result:", result)

# Run it
good_calculator()