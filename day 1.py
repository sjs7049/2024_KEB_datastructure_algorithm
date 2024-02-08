def factorial(number) -> int:
    pass

def nCr(n, r) -> int:
    '''
    조합을 계산하는 함수
    :param n: 전체 개수
    :param r: 선택 개수
    :return: nCr 값
    '''
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return numerator / denominator

if __name__ == "__main__":
    n,r = map(int, input("Input n, r").split())
    print(f'{n}C{r} = {nCr(n, r)}')
