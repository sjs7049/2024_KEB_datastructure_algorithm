def print_poly(f_x):
    term = len(f_x) - 1
    poly_str = "f(x) = "

    for i in range(len(fx)):
        coef = f_x[i]

        if coef == 0:
            term -= 1
            continue
        if coef >= 0 and i != 0:
            poly_str += "+"
        poly_str += str(coef) + "x^" + str(term) + " "
        term -= 1

    return poly_str


def calc_poly(x_val, f_x):
    ret_value = 0
    term = len(f_x) - 1

    for i in range(len(fx)):
        coef = f_x[i]
        ret_value += coef * pow(x_value, term)
        term -= 1

    return ret_value


fx = [7, -4, 0, 5]

if __name__ == "__main__":
    f_str = print_poly(fx)
    print(f_str)

    x_value = int(input("X 값 : "))

    pxValue = calc_poly(x_value, fx)
    print(pxValue)


