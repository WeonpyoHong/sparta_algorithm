input = 20

# Fibo(N) = Fibo(N-1) + Fibo(N-2)
def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    result = fibo_recursion(n-1) + fibo_recursion(n-2)
    return result


print(fibo_recursion(input))  # 6765



# input = 100 이 되면 값이 나오지 않을 정도로 오래걸림

# 동적계획법
# 이미 했던 작업의 반복을 피하기 위해서, 했던 작업을 기업하기 위해 동적 계획법을 이용