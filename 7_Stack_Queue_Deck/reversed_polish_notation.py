import A_stack


def reversed_polish_notation(sentence: str):
    for token in sentence:
        if token == ' ':
            continue
        if token.isdigit():
            A_stack.push(int(token))
        else:
            y = A_stack.pop()
            x = A_stack.pop()
            if token == '+':
                z = x + y
            elif token == '-':
                z = x - y
            elif token == '*':
                z = x * y
            else:
                z = x // y
            A_stack.push(z)
    return A_stack.pop()


print(reversed_polish_notation('2 7 5 * +'))