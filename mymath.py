# def factorial(number) -> int:
#     '''
#     factorial by repitition
#     :param number: number (int)
#     :return: factorial result
#     '''
#     result = 1
#     for i in range(1, number):
#         result *= i
#     return result

def factorial(number) -> int:
    '''
    factorial by recursion
    :param number: number (int)
    :return: factorial result
    '''
    if number == 0 or number == 1:
        return 1
    return number * factorial(number-1)

def nCr(n, r) -> int:
    '''
    combination function
    :param n: 전체 개수
    :param r: 선택 개수
    :return: nCr 값
    '''
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return int(numerator / denominator)