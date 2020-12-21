
# 회문검사 구현하기(재귀함수를 이용해서)

input = "소주만병만주소"

# 재귀의 원리 ===> "소주만병만주소" ===> "주만병만주" ===> "만병만" ===> "병"

# is_palindrome(string)
# 맨앞뒤 검사를 했다면
# is_palindrome(string[1:-1])


def is_palindrome(string):
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True
    return is_palindrome(string[1:-1])


print(is_palindrome(input))


# "가나다라마바사"[0:3]
# "가나다"

# "가나다라마바사"[1:5]
# "나다라마"

# "가나다라마바사"[0:-2]
# "가나다라마"

# "가나다라마바사"[1:-4]
# "나다"