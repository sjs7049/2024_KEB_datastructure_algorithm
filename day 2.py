class Node:
    def __init__ (self):
        self.data = None
        self.link = None

def process_minus(data_array):
    global head, current
    count_odd = 0
    count_even = 0
    for i in data_array:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    if count_odd > count_even:
        res = 1
    else:
        res = 0

    current = head
    while True:
        if current.data % 2 == res:
            current.data *= -1
        if current.link == head:
            break
        current = current.link

def process_toggle(data_array):
    global head, current
    cnt_positive = 0
    cnt_negative = 0
    cnt_zero = 0

    for i in data_array:
        if i > 0:
            cnt_positive += 1
        elif i < 0:
            cnt_negative += 1
        else:
            cnt_zero += 1

    print(f"양수 : {cnt_positive}, 음수 : {cnt_negative}, 0 : {cnt_zero}")

    current = head
    while True:
        current.data *= -1
        if current.link == head:
            break
        current = current.link

def print_nodes(start):
    current = start
    if current.link is None :
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()


import random
head, current, pre = None, None, None
data_array = [random.randint(-100, 100) for _ in range(7)]

if __name__ == "__main__":
    node = Node()
    node.data = data_array[0]
    head = node
    node.link = head

    for data in data_array[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head

    print_nodes(head)
    process_toggle(data_array)
    print_nodes(head)




