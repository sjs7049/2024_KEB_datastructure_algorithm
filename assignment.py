
def notation_recursion(base, number):
    if number < base:
        print(number_char[number], end='')
    else:
        notation_recursion(base, number // base)
        print(number_char[number % base], end='')

number_char = ['0','1','2','3','4','5','6','7','8','9',
               'A','B','C','D','E','F']

if __name__ == "__main__":
    print(f"10진수 입력 --->", end=' ')
    n = int(input())

    print("\n2진수 :", end=' ')
    notation_recursion(2,n)
    print("\n8진수 :", end=' ')
    notation_recursion(8,n)
    print("\n16진수 :", end=' ')
    notation_recursion(16,n)