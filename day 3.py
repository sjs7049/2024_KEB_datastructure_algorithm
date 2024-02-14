def decimal_to_octal(number) -> int:
    '''
    decimal number to octal number
    :param number: int (base decimal)
    :return: str (base octal)
    '''
    if number < 8:
        return str(number)
    else:
        return decimal_to_octal(number // 8) + str(n % 8)

n = int(input("Input decimal number: "))
print(decimal_to_octal(n))