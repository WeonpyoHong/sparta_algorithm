
# 회문검사 구현하기
# "소주만병만주소"

input = "abcba"


# for문을 이용해서 회문검사 구현하기

def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - 1 - i]:
            return False

    return True


print(is_palindrome(input))
