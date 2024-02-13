import random

class Node:
    def __init__(self):
        self.data = None
        self.link = None

def print_nodes(start):
    current = start
    if current is None:
        return
    print(current.data, end=' ')
    while current.link is not None:
        current = current.link
        print(current.data, end=' ')
    print()

def lotto_list(number):
    global head, current, pre

    node = Node()
    node.data = number
    if head is None:
        head = node
        return

    if head.data > number:
        node.link = head
        head = node
        return

    current = head
    while current.link is not None:
        pre = current
        current = current.link
        if current.data > number:
            pre.link = node
            node.link = current
            return

    current.link = node



head, current, pre = None, None, None

if __name__ == "__main__":
    cnt_lotto = 0
    while True:
        lotto = random.randint(1,45)
        cnt_lotto += 1
        lotto_list(lotto)
        if cnt_lotto == 6:
            break

    print_nodes(head)