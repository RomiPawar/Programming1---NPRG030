import sys

def evaluate(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    tokens = expression.split()

    for token in reversed(tokens):
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(int(token))
        elif token in operators:
            if len(stack) < 2:
                return "ERROR"
            operand1 = stack.pop()
            operand2 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                if operand2 == 0:
                    return "ERROR"
                stack.append(operand1 // operand2)
        else:
            return "ERROR"

    if len(stack) != 1:
        return "ERROR"
    return stack[0]

if __name__ == "__main__":
    try:
        expression = input().strip()
    except EOFError:
        sys.exit(1)

    result = evaluate(expression)
    print(result)
