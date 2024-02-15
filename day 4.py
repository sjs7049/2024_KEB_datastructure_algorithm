import tkinter as tk

memo = [0 if i == 0 else 1 if i == 1 else None for i in range(100)]

def fibo_memoization(number) -> int :
    '''
    fibonacci function by recursion with memoization.
    :param number: integer number
    :return: integer number
    '''
    global memo
    if memo[number] is not None: # 한 번 계산한 결과를 가지고 있으면 바로 리턴
        return memo[number]

    result = fibo_memoization(number - 1) + fibo_memoization(number - 2)
    memo[number] = result
    return result

def process_fibonacci():
    number = int(en_input_number.get())
    lbl_display_fibonacci_recursion.config(text=f"fibonacci({number}) = {fibo_memoization(number)}")

if __name__ == "__main__":
    w = tk.Tk() # create window object
    w.title("Fibonacci")
    w.geometry("250x100")

    # create widget
    lbl_display_fibonacci_recursion = tk.Label(w, text='Fibonacci by memoization')
    en_input_number = tk.Entry(w)
    btn_click = tk.Button(w, text='Click', command=process_fibonacci) # bind function

    # layout
    lbl_display_fibonacci_recursion.pack()
    en_input_number.pack(fill="x")
    btn_click.pack(fill="x")

    en_input_number.focus()
    w.mainloop() # 끌 때까지 계속 루프 돌음


# n = int(input("Input the number : ")) # Input box
# print(f"fibonacci({n}) =  {fibo_memoization(n)}") # Label