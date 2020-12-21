s = "(())()"
s = "()()()()"


def is_correct_parenthesis(string):
    count = len(string)

    # 짝수개인지 확인
    if count % 2 != 0:
        return False
    # 시작"(" 과 끝 확인 ")"
    if string[0] == ")" or string[count - 1] == "(":
        return False
    # 갯수세어서 각각 짝 앞뒤가 맞는지 확인
    left_count = 0
    right_count = 0
    for s in string:
        if s == "(":
            left_count += 1
            continue
        if s == ")":
            right_count += 1
            continue
        return False
    if left_count != right_count:
        return False
    # 반으로 나눠서 앞부분에 "("가 더 많은지 확인 (")"가 더 많으면 False)
    left_count = 0
    right_count = 0
    mid = count // 2
    for s in string[0:mid]:
        if s == "(":
            left_count += 1
            continue
        if s == ")":
            right_count += 1
            continue
    if left_count < right_count:
        return False

    return True


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!