def fibo_recursion(number) -> int :
    '''
    fibonacci function by recursion.
    :param number: integer number
    :return: integer number
    '''
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibo_recursion(number - 1) + fibo_recursion(number - 2)

def fibo_repetition(number):
    '''
    fibonacci function by repetion.
    :param number: integer number
    :return: integer number
    '''
    a = 0
    b = 1
    for _ in range(number):
        a,b = b, a + b
    return a

memo = [None for _ in range(100)]
def fibo_memoization(number, memo) -> int :
    '''
    fibonacci function by recursion with memoization.
    :param number: integer number
    :return: integer number
    '''
    if memo[number] is not None: # 한 번 계산한 결과를 가지고 있으면 바로 리턴
        return memo[number]

    if number < 2:
        result = number
    else:
        result = fibo_memoization(number - 1, memo) + fibo_memoization(number - 2, memo)
    memo[number] = result
    return result

n = int(input("Input the number : "))
for i in range(0, n+1):
    print(fibo_memoization(i, memo), end=' ')
