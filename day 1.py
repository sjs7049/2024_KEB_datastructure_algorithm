import mymath

if __name__ == "__main__":
    n,r = map(int, input("Input n, r : ").split())
    print(f'{n}C{r} = {mymath.nCr(n, r)}')
