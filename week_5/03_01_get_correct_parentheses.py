from collections import deque

balanced_parentheses_string = "()))((()"

def get_correct_parentheses(string):

    if string == "":
        return ""

    stack = []
    count = 0
    is_balanced = False

    for s in string:
        if s == "(":
            stack.append("(")
            count += 1
        else:
            stack.pop()
            count -= 1

    if count == 0:
        is_balanced = True



    if stack:
        return True
    else:
        return False

    return

print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!