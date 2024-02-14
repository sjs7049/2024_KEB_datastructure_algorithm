import random
from math import *

class Node:
    def __init__(self):
        self.data = None
        self.link = None

def print_nodes(start):
    current = start
    if current is None:
        return

    while current.link != head:
        current = current.link
        x,y = current.data[1:]
        print(f'{current.data[0]} 편의점, 거리: {sqrt(x**2 + y**2)}')
    print()

def make_store_list(store):
    global head, current, pre

    node = Node()
    node.data = store

    if head is None:
        head = node
        node.link = head
        return

    x_node, y_node = node.data[1:]
    node_distance = sqrt(x_node**2 + y_node**2)
    x_head, y_head = head.data[1:]
    head_distance = sqrt(x_head**2 + y_head**2)

    if head_distance > node_distance:
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        x_current, y_current = current.data[1:]
        current_distance = sqrt(x_current**2 + y_current**2)
        if current_distance > node_distance:
            pre.link = node
            node.link = current
            return

    current.link = node
    node.link = head


head, current, pre = None, None, None

if __name__ == "__main__":
    store_array = []
    store_name = 'A'

    for _ in range(10):
        store = (store_name, random.randint(1,100), random .randint(1,100))
        store_array.append(store)
        store_name = chr(ord(store_name) + 1)

    for i in store_array:
        make_store_list(i)

    print_nodes(head)
