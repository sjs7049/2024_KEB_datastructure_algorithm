def is_stack_full():
    global size, top
    return top >= size - 1

def is_stack_empty():
    global top
    return top == -1

def push(data):
    global stack, top
    if is_stack_full():
        return None
    top += 1
    stack[top] = data

def pop():
    global stack, top
    if is_stack_empty():
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

size = 10
top = -1
stack = [None for _ in range(size)]

if __name__ == "__main__":
    color_array = ['주황', '초록', '파랑', '보라', '빨강', '노랑']

    print("과자 집에 가는 길 :", end=' ')
    for color in color_array:
        push(color)
        print(f"{color} --->", end=' ')
    print("과자집")

    print("우리 집에 가는 길 :", end=' ')
    while True:
        color = pop()
        if color is None:
            break
        print(f"{color} --->", end=' ')
    print("우리집")