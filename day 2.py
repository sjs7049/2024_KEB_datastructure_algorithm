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

def insert_data(name_email):
    global head, current, pre
    print_nodes(head)

    node = Node()
    node.data = name_email

    if head == None:
        head = node
        return

    if head.data[1] > name_email[1]:
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data[1] > name_email[1]:
            pre.link = node
            node.link = current
            return

    current.link = node

head, current, pre = None, None, None

if __name__ == "__main__":
    while True:
        name = input("이름--> ")
        if name == "" or name is None:
            break
        email = input("이메일--> ")
        insert_data([name, email])
        print_nodes(head)