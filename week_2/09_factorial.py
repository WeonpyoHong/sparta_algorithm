
# 재귀함수
# 팩토리얼 구현하기

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)


print(factorial(5))