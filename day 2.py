class Node:
    def __init__(self):
        self.data = None
        self.front_link = None
        self.back_link = None

def print_nodes(start):
    current = start
    if current.back_link is None:
        return
    print("정방향 ---> ", end=' ')
    print(current.data, end=' ')
    while current.back_link is not None:
        current = current.back_link
        print(current.data, end=' ')
    print()

    print("역방향 ---> ", end=' ')
    print(current.data, end=' ')
    while current.front_link is not None:
        current = current.front_link
        print(current.data, end=' ')
    print()

head, current, pre = None, None, None
name_array = ['다현', '정연', '쯔위', '사나', '지효']
if __name__ == "__main__":
    node = Node()
    node.data = name_array[0]
    head = node

    for name in name_array[1:]:
        pre = node
        node = Node()
        node.data = name
        pre.back_link = node
        node.front_link = pre

    print_nodes(head)