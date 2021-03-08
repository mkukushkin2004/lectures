import A_stack


def is_braces_sequence_correct(s: str):
    for brace in s:
        if brace not in "()[]":
            continue
        if brace in "([":
            A_stack.push(brace)
        else:
            if A_stack.is_empty():
                return False
            left = A_stack.pop()
            if left == "(":
                right = ")"
            else:
                right = "]"
            if right != brace:
                return False
    return A_stack.is_empty()
