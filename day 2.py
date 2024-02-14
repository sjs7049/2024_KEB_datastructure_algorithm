class Node:
    def __init__(self):
        self.data = None
        self.forward_link = None
        self.reverse_link = None

def print_nodes(start):
    current = start
    if current.forward_link is None:
        return
    print("과자 집에 가는 길 : ", end=' ')
    print(f"{current.data} --->", end=' ')
    while current.forward_link is not None:
        current = current.forward_link
        print(f"{current.data} --->", end=' ')
    print('과자집')

    print("우리 집에 가는 길 : ", end=' ')
    print(f"{current.data} --->", end=' ')
    while current.reverse_link is not None:
        current = current.reverse_link
        print(f"{current.data} --->", end=' ')
    print('우리집')


head, current, pre = None, None, None
color_array = ['주황', '초록', '파랑', '보라', '빨강', '노랑']

if __name__ == "__main__":
    node = Node()
    node.data = color_array[0]
    head = node

    for color in color_array[1:]:
        pre = node
        node = Node()
        node.data = color
        pre.forward_link = node
        node.reverse_link = pre

    print_nodes(head)