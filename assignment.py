class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def print_graph(g):
    print("  ", end=' ')
    for i in range(gSize):
        print(submarine_cable[i], end=' ')
    print()

    for row in range(gSize):
        print(submarine_cable[row], end=' ')
        for col in range(gSize):
            print(f"{g.graph[row][col]:>2}", end='  ')
        print()
    print()

def find_vertex(g, find_vtx) :
    stack = []
    visited_ary = []

    current = 0
    stack.append(current)
    visited_ary.append(current)

    while len(stack) != 0:
        next = None
        for vertex in range(gSize):
            if g.graph[current][vertex] != 0:
                if vertex in visited_ary:
                    pass
                else:
                    next = vertex
                    break

        if next is not None:
            current = next
            stack.append(current)
            visited_ary.append(current)
        else:
            current = stack.pop()

    return find_vtx in visited_ary

G1 = None
submarine_cable = ["서울", "뉴욕", "런던", "북경", "방콕", "파리"]
서울, 뉴욕, 런던, 북경, 방콕, 파리 = 0,1,2,3,4,5

gSize = 6
G1 = Graph(gSize)
G1.graph[서울][뉴욕] = 80; G1.graph[서울][북경] = 10
G1.graph[뉴욕][서울] = 80; G1.graph[뉴욕][북경] = 40; G1.graph[뉴욕][방콕] = 70
G1.graph[런던][방콕] = 30; G1.graph[런던][파리] = 60
G1.graph[북경][서울] = 10; G1.graph[북경][뉴욕] = 40; G1.graph[북경][방콕] = 50
G1.graph[방콕][뉴욕] = 70; G1.graph[방콕][런던] = 30; G1.graph[방콕][북경] = 50; G1.graph[방콕][파리] = 20
G1.graph[파리][런던] = 60; G1.graph[파리][방콕] = 20

if __name__ == "__main__":
    print("## 해저 케이블 연결을 위한 전체 연결도 ##")
    print_graph(G1)

    edge_ary = []
    for i in range(gSize):
        for j in range(gSize):
            if G1.graph[i][j] != 0:
                edge_ary.append([G1.graph[i][j], i, j])

    edge_ary.sort(key=lambda data: data[0])

    new_ary = []
    for i in range(0, len(edge_ary), 2):
        new_ary.append(edge_ary[i])

    index = 0
    while len(new_ary) > gSize - 1:
        start = new_ary[index][1]
        end = new_ary[index][2]
        save_cost = new_ary[index][0]

        G1.graph[start][end] = 0
        G1.graph[end][start] = 0

        startYN = find_vertex(G1, start)
        endYN = find_vertex(G1, end)

        if startYN and endYN:
            del new_ary[index]
        else:
            G1.graph[start][end] = save_cost
            G1.graph[end][start] = save_cost
            index += 1

    print("## 가장 효율적인 해저 케이블 연결도 ##")
    print_graph(G1)