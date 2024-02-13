def print_poly(f_x):
    poly_str = "f(x) = "

    for i in range(len(f_x)):
        term = f_x[i][0]
        coef = f_x[i][1]

        if coef >= 0:
            poly_str += "+"
        poly_str += str(coef) + "x^" + str(term) + " "

    return poly_str


def calc_poly(x_val, f_x):
    ret_value = 0

    for i in range(len(fx)):
        term = f_x[i][0]
        coef = f_x[i][1]
        ret_value += coef * pow(x_value, term)

    return ret_value

fx = [[300, 7], [20, -4], [0, 5]]

if __name__ == "__main__":
    pStr = print_poly(fx)
    print(pStr)

    x_value = int(input("X 값-->"))

    pxValue = calc_poly(x_value, fx)
    print(pxValue)
